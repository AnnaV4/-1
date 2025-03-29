# Models

## Operation

- normative_time: IntegerField ("Нормативное время на выполнение операции")
- allocated_resources: IntegerField ("Количество выделяемых ресурсов")
- resource_availability_coefficient: FloatField ("Коэффициент доступности ресурсов")
- labor_productivity_coefficient: FloatField ("Коэффициент производительности труда")
- duration_estimate: FloatField ("Оценка длительности")

---

### Описание полей

normative_time  
Целочисленное значение нормативного времени выполнения операции (в минутах)

allocated_resources  
Количество единиц ресурсов (персонал/оборудование), выделенных для операции

resource_availability_coefficient  
Доля доступности ресурсов (0.0-1.0, где 1.0 = 100% доступность)

labor_productivity_coefficient  
Показатель эффективности труда (0.0-1.0, где 1.0 = 100% производительность)

duration_estimate  
Расчетная длительность операции с учетом всех факторов (в минутах)

---

### Пример использования

```python
# Создание операции
op = Operation.objects.create(
    normative_time=120,
    allocated_resources=5,
    resource_availability_coefficient=0.85,
    labor_productivity_coefficient=0.92,
    duration_estimate=98.7
)

# Получение операций с высокой производительностью
high_productivity_ops = Operation.objects.filter(
    labor_productivity_coefficient__gte=0.9
)
```