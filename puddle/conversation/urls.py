from django.urls import path

from .views import *


app_name = 'conversation'

urlpatterns = [
    path('', inbox, name='inbox'),
    path('new/<int:item_pk>/', new_conversation, name='new'),
    path('<int:pk>/', detail, name='detail'),
]
