from django.urls import path
from . import views


urlpatterns = [
    path('', views.readAll, name="readAll"),
    path('create/', views.create, name="rate_create"),
]