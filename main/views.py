from django.shortcuts import render
from . import models 
from . import forms as f
from django import forms
from django.http import HttpResponseRedirect
from main.forms import ProductForms
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers


def home(request):
    my_obats = models.Item.objects.all()    
    banyak_item = my_obats.count()
    context = {
        "nama_project" : "ManageVent",
        "developer" : "Daveen",
        "nama" : "Rakha Davin Bani Alamsyah",
        "kelas": "PBP F",
        "title":"ManageVent",
        "app" : "main",
        "pages" : "Home",
        "items":my_obats,
        "banyak_item" : banyak_item,
        
    }
    

    return render(request,"home.html",context)


def creat_data_obat (request) :
  
    
    form = ProductForms(request.POST or None)
    if (form.is_valid() and request.method == "POST"):

        form.save()
        return HttpResponseRedirect(reverse('main:create_obat'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = models.Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


    
def show_json(request):
    data = models.Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = models.Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = models.Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = models.Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def expired(request):
    if request.method == 'POST':
        form = f.ExpiredForms(request.POST)
        if form.is_valid():
            expired_field = form.changed_data['expired']

    else:
        form = f.ExpiredForms()

    return render(request, 'home.html', {'form': form})
    