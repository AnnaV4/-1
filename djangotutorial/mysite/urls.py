from django.contrib import admin
from django.urls import include, path
from polls.nocodb import get_nocodb_data
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
       openapi.Info(
           title="My API",
           default_version='v1',
           description="API documentation for My Django Project",
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('polls.urls')),

    path("admin/", admin.site.urls),
    # project_name/urls.py

 # Админка Django
    path('polls/', include('polls.urls')), 
    path('nocodb-data/', get_nocodb_data, name='nocodb_data'), # Подключение маршрутов из myapp
]



