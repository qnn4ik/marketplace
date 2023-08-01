from django.urls import path

from item import views
from .views import *


app_name = 'item'

urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
    path('new/', views.new, name='new'),
]
