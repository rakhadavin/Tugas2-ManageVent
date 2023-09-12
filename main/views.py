from django.shortcuts import render


def home(request):
    context = {
        "nama_project" : "ManageVent",
        "developer" : "Daveen",
        "nama" : "Rakha Davin Bani Alamsyah",
        "kelas": "PBP F",
        "title":"ManageVent",
        "app" : "main",
        "pages" : "Home",
        
    }
    return render(request,"home.html",context)
