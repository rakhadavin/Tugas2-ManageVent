
from django.urls import path
from main.views import  show_xml, show_json, show_xml_by_id, show_json_by_id 
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home, name='home'),
    path('create-obat/', views.create_data_obat, name='create_obat'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('nambah/<str:id_obat>/', views.nambah_obat, name='nambah_obat'),
    path('kurangi/<str:id_obat>/', views.kurangi_obat, name='kurangi_obat'),
    path('delete/<str:id_obat>/', views.delete_obat, name='delete_obat'),
    
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    
]
