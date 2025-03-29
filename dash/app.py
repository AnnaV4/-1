import dash
from dash import html, dcc
from dash import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests

# Функция получения данных из NocoDB
def get_nocodb_data():
    url = "http://backend:8000/nocodb-data/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            records = data.get('records', [])
            print("Полученные данные:", records)
            cleaned_records = [
                {k: v for k, v in record.items() if not k.startswith('_nc_m2m_')}
                for record in records
            ]
            return pd.DataFrame(cleaned_records)
        else:
            print("Ошибка при получении данных:", response.status_code)
            return pd.DataFrame()
    except Exception as e:
        print(f"Ошибка соединения: {e}")
        return pd.DataFrame()

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Базовый макет приложения
app.layout = html.Div([
    html.H1('Анализ производительности операций'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # обновление каждую секунду при первой загрузке
        n_intervals=0,
        max_intervals=1   # выполняется только один раз при загрузке
    ),
    html.Div(id='dashboard-content')
])

# Callback для обновления содержимого при загрузке
@app.callback(
    Output('dashboard-content', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_dashboard(n):
    # Получаем данные
    df = get_nocodb_data()

    # Проверяем, что DataFrame не пустой
    if df.empty:
        return html.P('Нет данных для отображения. Проверьте соединение с NocoDB.')
    
    # Преобразуем даты
    if 'CreatedAt' in df.columns:
        df['CreatedAt'] = pd.to_datetime(df['CreatedAt'])
    if 'UpdatedAt' in df.columns:
        df['UpdatedAt'] = pd.to_datetime(df['UpdatedAt'], errors='coerce')

    # Преобразуем числовые колонки и заполняем пропущенные значения
    numeric_cols = [
        'Нормативное время на выполнение операции',
        'Количество выделяемых ресурсов',
        'Коэффициент доступности ресурсов',
        'Коэффициент производительности труда',
        'Оценка длительности'
    ]
    
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            # Заменяем NaN на 0 для числовых колонок
            df[col] = df[col].fillna(0)

    # Создаем визуализации
    if 'Оценка длительности' in df.columns:
        fig_duration = px.bar(df, 
                            x='Id', 
                            y='Оценка длительности',
                            title='Оценка длительности операций',
                            labels={'Оценка длительности': 'Длительность', 'Id': 'ID операции'})
    else:
        fig_duration = px.bar(title='Нет данных о длительности операций')
    if 'Количество выделяемых ресурсов' in df.columns and 'Коэффициент производительности труда' in df.columns:
        # Создаем копию данных без строк с NaN для scatter plot
        scatter_df = df.dropna(subset=['Количество выделяемых ресурсов', 'Коэффициент производительности труда', 'Оценка длительности'])
        
        fig_resources = px.scatter(scatter_df if not scatter_df.empty else df, 
                                x='Количество выделяемых ресурсов', 
                                y='Коэффициент производительности труда',
                                size='Оценка длительности' if 'Оценка длительности' in df.columns else None,
                                color='Id',
                                title='Зависимость производительности от количества ресурсов',
                                labels={
                                    'Количество выделяемых ресурсов': 'Ресурсы',
                                    'Коэффициент производительности труда': 'Производительность (%)',
                                    'Id': 'ID операции'
                                })
    else:
        fig_resources = px.scatter(title='Нет данных о ресурсах и производительности')

    # Определяем колонки для таблицы
    table_columns = [
        {'name': 'ID', 'id': 'Id'},
        {'name': 'Нормативное время', 'id': 'Нормативное время на выполнение операции'},
        {'name': 'Количество ресурсов', 'id': 'Количество выделяемых ресурсов'},
        {'name': 'Доступность ресурсов', 'id': 'Коэффициент доступности ресурсов'},
        {'name': 'Производительность (%)', 'id': 'Коэффициент производительности труда'},
        {'name': 'Оценка длительности', 'id': 'Оценка длительности'},
        {'name': 'Создано', 'id': 'CreatedAt'},
        {'name': 'Обновлено', 'id': 'UpdatedAt'},
    ]

    # Рассчитываем статистики только по непустым значениям
    stats = []
    numeric_cols_present = [col for col in numeric_cols if col in df.columns]
    
    for col in numeric_cols_present:
        non_null_values = df[col][df[col].notna()]
        if len(non_null_values) > 0:
            stats.append(html.P(f"Среднее {col.split()[-1]}: {non_null_values.mean():.2f}"))
            stats.append(html.P(f"Максимальное {col.split()[-1]}: {non_null_values.max():.2f}"))
            stats.append(html.P(f"Минимальное {col.split()[-1]}: {non_null_values.min():.2f}"))
            stats.append(html.Br())

    # Возвращаем содержимое dashboard
    return [
        html.Div([
            html.H3('Общая статистика'),
            html.P(f"Всего операций: {len(df)}"),
            html.P(f"Из них с полными данными: {len(df.dropna())}"),
            *stats
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        
        html.Div([
            dcc.Graph(figure=fig_duration),
            dcc.Graph(figure=fig_resources),
        ], style={'width': '65%', 'display': 'inline-block', 'float': 'right'}),
        
        html.Div([
            html.H3('Детальная информация по операциям'),
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=table_columns,
                style_table={'overflowX': 'auto'},
                style_cell={
                    'minWidth': '100px', 'width': '150px', 'maxWidth': '300px',
                    'whiteSpace': 'normal',
                    'textAlign': 'left'
                },
                filter_action='native',
                sort_action='native',
                page_size=10
            )
        ], style={'marginTop': '20px', 'clear': 'both'})
    ]

# Запуск приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)  