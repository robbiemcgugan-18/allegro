"""dynamica_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include
from dynamica_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='user_login'),
    path('menu/', views.menu, name='menu'),
    path('menu/request-music/', views.request_music, name='request_music'),
    path('menu/calendar/', views.calendar, name='calendar'),
    path('menu/manage-calendar/', views.manage_calendar, name='manage_calendar'),
    path('menu/add-music/', views.add_music, name='add_music'),
    path('menu/my-requests/', views.my_requests, name='my_requests'),
    path('menu/view-requests/', views.view_requests, name='view_requests'),
    path('logout/', views.user_logout, name='logout'),
    path('permission-denied/', views.permission_denied, name='permission_denied'),
]
