from django.contrib import admin
from django.urls import path
from libros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_libros, name='lista_libros'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libro/nuevo/', views.crear_libro, name='crear_libro'),
    path('libro/editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('libro/eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
]
