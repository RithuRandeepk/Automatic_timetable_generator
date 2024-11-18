"""
URL configuration for timetable_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_course/', views.create_course, name='create_course'),
    path('create_subject/', views.create_subject, name='create_subject'),
    path('add_period/', views.add_period, name='add_period'),
    path('list_period/', views.list_period, name='list_period'),
    path('', views.course_list, name='course_list'),
    path('delete_course/<int:pk>/', views.delete_course, name='delete_course'), 
    path('update_course/<int:pk>/', views.update_course, name='update_course'), 
    path('staff_list/', views.staff_list, name='staff_list'),
    path('create_staff/', views.create_staff, name='create_staff'),
    path('update_staff/<int:pk>/', views.update_staff, name='update_staff'),
    path('delete_staff/<int:pk>/', views.delete_staff, name='delete_staff'),
    path('generate_timetable/<int:course_id>/', views.generate_timetable_view, name='generate_timetable'),
    path('timetable_list/<int:course_id>/', views.timetable_list, name='timetable_list'),


]
