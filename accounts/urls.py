from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:pk_test2>', views.updateOrder, name='update_order'),


]