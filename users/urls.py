from django.urls import path, include
from users import views


urlpatterns = [
    path('users/', views.UserCreation.as_view(), name='user-list')
]
