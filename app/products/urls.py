from django.urls import path

from . import views

urlpatterns = [

    path('', views.AllProducts.as_view()),
    path('categorys/', views.AllCategorys.as_view())

]