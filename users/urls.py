from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.register, name='signup'),
]