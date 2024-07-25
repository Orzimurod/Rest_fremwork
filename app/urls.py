from django.urls import path
from app.views import users_view

urlpatterns = [
    path('users/',users_view, name='users')
]
