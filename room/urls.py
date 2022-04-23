from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('<slug:room_slug>/', views.room_detail, name='room_detail')
]
