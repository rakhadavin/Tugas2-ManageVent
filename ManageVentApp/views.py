from django.shortcuts import render



def homePages(request):

    context = {
        "nama_project" : "ManageVent",
        "developer" : "Daveen",
        "nama" : "Rakha Davin Bani Alamsyah",
        "kelas": "PBP F",
        "title":"ManageVent",
        "app" : "Home Page",
        "pages" : "Home",

        
    }
    return render(request,'homePages.html',context)
