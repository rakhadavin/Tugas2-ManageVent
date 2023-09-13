from django.shortcuts import render
from . import models


def home(request):
    my_items = models.Item.objects.all()
    context = {
        "nama_project" : "ManageVent",
        "developer" : "Daveen",
        "nama" : "Rakha Davin Bani Alamsyah",
        "kelas": "PBP F",
        "title":"ManageVent",
        "app" : "main",
        "pages" : "Home",
        "item":my_items
        
    }
    return render(request,"home.html",context)
