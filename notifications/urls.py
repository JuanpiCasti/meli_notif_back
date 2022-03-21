
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListNotifications.as_view())
]