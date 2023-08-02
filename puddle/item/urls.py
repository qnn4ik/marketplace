from django.urls import path

from .views import *


app_name = 'item'

urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
    path('new/', NewItem.as_view() , name='new'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/edit/', EditItem.as_view(), name='edit'),
]
