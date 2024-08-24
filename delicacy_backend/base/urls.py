from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('products/', views.getProducts),
    path('product/<str:id>/', views.getProductById),
]