from django.urls import path

from .views import *


app_name = 'item'

urlpatterns = [
    path('<int:pk>/', ItemDetail.as_view(), name='detail'),
    path('new/', CreateItem.as_view(), name='new'),
    path('<int:pk>/delete/', delete_item, name='delete'),
    path('<int:pk>/edit/', EditItem.as_view(), name='edit'),
]
