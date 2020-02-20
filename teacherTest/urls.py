from django.contrib import admin
from django.urls import path,include
import rate.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/',include('member.urls')),
    path('rate/', include('rate.urls')),
    path('',rate.views.readAll, name="home"),
]
