from django.urls import path
from . import views

urlpatterns = [
    path('', views.alltodos, name='alltodos'),
    path('delete/<int:pk>/', views.deleteItem, name='deleteItem'),
    path('update/<int:pk>/', views.updateItem, name='updateItem')
]