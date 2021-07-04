from django.urls import path

from . import views

urlpatterns = [

    path('', views.ProductsList.as_view()),
    path('create/', views.CreateProduct.as_view()),

]