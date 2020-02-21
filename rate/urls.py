from django.urls import path
from . import views


urlpatterns = [
    path('', views.readAll, name="rate_list"),
    path('create/', views.create, name="rate_create"),
    path('edit/', views.edit, name="rate_edit"),
    path('update/<int:rate_id>', views.update, name="rate_update"),
    #삭제 url 추가
    path('delete/<int:rate_id>', views.delete, name="rate_delete"),
]