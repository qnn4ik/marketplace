from django.urls import path

from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardHome.as_view(), name='index'),
]
