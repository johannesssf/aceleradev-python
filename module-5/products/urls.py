from django.urls import path

from products import views

urlpatterns = [
    path('list', views.list_products, name='list'),
    path('create', views.create_produtct, name='create')
]