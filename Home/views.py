from django.shortcuts import render

def landingPages(request):
    
    context = {"app":"ManageVent",
               "pages" : "Home",}
    return render(request,  'landingPages.html',context)

