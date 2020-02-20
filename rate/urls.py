from django.urls import path
from . import views

urlpatterns = [
    path('', views.readAll, name='rate_list'),
    path('create/', views.create, name="rate_create"),
]