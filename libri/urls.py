from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libri, name='lista_libri'),
    path('<int:pk>/', views.dettaglio_libro, name='dettaglio_libro'),
    path('aggiungi/', views.aggiungi_libro, name='aggiungi_libro'),
    path('<int:pk>/modifica/', views.modifica_libro, name='modifica_libro'),
    path('<int:pk>/elimina/', views.elimina_libro, name='elimina_libro'),
]