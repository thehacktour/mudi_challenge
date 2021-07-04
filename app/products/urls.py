from django.urls import path

from . import views

urlpatterns = [

    path('', views.AllProducts.as_view()),
    path('categorys/', views.AllCategorys.as_view()),
    path('create/', views.AddProduct.as_view()),
    path('products/<int:id>/', views.ProductById.as_view()),


]