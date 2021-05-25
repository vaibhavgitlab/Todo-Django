from tod.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('add/',Add,name='add'),
    path('del/<int:pid>',Delete,name='del'),
    path('edit/<int:pid>',Edit,name='edit'),
]
