from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ejemplo de URL administrativa
    path('', include('api.urls')),  # Incluir las URLs de tu API
]