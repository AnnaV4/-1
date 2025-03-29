from django.contrib import admin
from django.urls import include, path
from polls.nocodb import get_nocodb_data

urlpatterns = [
    path("admin/", admin.site.urls),
    # project_name/urls.py

 # Админка Django
    path('polls/', include('polls.urls')), 
    path('nocodb-data/', get_nocodb_data, name='nocodb_data'), # Подключение маршрутов из myapp
]



