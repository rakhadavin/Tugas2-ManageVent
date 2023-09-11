from django.shortcuts import render


def home(request):
    context = {
        "nama_project" : "ManageVent",
        "developer" : "Daveen",
        "nama" : "Rakha Davin Bani Alamsyah",
        "kelas": "PBP F",
        "title":"ManageVent",
        "app" : "Main",
        "pages" : "Home",
        
    }
    return render(request,"home.html",context)
