from django.urls import path
from authentication.views import login
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', views.logout, name='logout'),
    
]