from django.urls import path
from . import views

urlpatterns = [

    path('<int:value>/', views.single_post_page),
    path('', views.index),
]