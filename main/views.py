from django.shortcuts import render
from . import models 
from . import forms as f
from django import forms
from django.http import HttpResponseNotFound, HttpResponseRedirect
from main.forms import ProductForms
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.models import User 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def get_product_json(request):
    my_obats = models.Item.objects.all()
    return HttpResponse(serializers.serialize("json", my_obats))


def get_product_by_id(request,id_obat):
    selected_item = models.Item.objects.get(id=id_obat)
    print(selected_item)

    return HttpResponse(serializers.serialize("json", selected_item))


@login_required(login_url='/login')
def home(request):
    my_obats = models.Item.objects.filter(user = request.user)    
    banyak_item = my_obats.count()
    last_item = my_obats.last()

    
    try:
            
        context = {
            "nama_project" : "ManageVent",
            "developer" : "Daveen",
            "nama" : request.user,
            "kelas": "PBP F",
            "title":"ManageVent",
            "app" : "main",
            "pages" : "Home",   
            "items":my_obats,
            "banyak_item" : banyak_item,
            "last_item":last_item,
            "last_login": request.COOKIES['last_login'],
            
        }
    except:
        return redirect("main:login")
    return render(request,"home.html",context)


def create_data_obat (request) :
    form = ProductForms(request.POST or None)
    if (form.is_valid() and request.method == "POST"):
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        form.save()
        
        product.user = request.user
        product.save()

        return redirect('main:home')

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

@csrf_exempt
# perbaiki filed nya
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = models.Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
def register (request):
    #buat form nya
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Selamat Akun Anda Berhasil Dibuat !')
            return redirect('main:home') ## mengarahkan ke url --> 'app_name:url_name
        # elif ( authenticate(request,request.POST.get('username'), request.POST.get('password')) is not none):
        #     messages.MessageFailure("Maaf akun sudah pernah terdaftar.")
        
    context = {'form': form}
    return render(request,"register.html",context)


def login_user (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password'  )
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:home")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Maaf, Password atau Username yang Anda masukan salah !')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, "Berhasil Logout!")
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
             

def nambah_obat(request,id_obat):
    selected_item = models.Item.objects.get(id=id_obat)
    if (  selected_item is not None):
        selected_item.amount +=1;
        selected_item.save()
        return HttpResponseRedirect(reverse('main:home'))

    return render(request,'home.html')


        
        
def kurangi_obat(request,id_obat):
    selected_item = models.Item.objects.get(id=id_obat)
    print("ini sebelum : " , selected_item.amount)
    if ( selected_item is not None ):
        if ( selected_item.amount <=0 ):
            messages.MessageFailure(request,"Stok Habis !")
        else:
                
            selected_item.amount -=1;
            selected_item.save()
            print("ini setelah  : " , selected_item.amount)
            return HttpResponseRedirect(reverse('main:home'))
    
        
    return HttpResponseRedirect(reverse('main:home'))





def delete_obat(request,id_obat):
    selected_item = models.Item.objects.get(id=id_obat)
    if  selected_item is not None:
        selected_item.delete()

    return HttpResponseRedirect(reverse('main:home'))
    
def user_profile(request,id_user):
    selected_user = User.objects.filter(id=id_user).first() #ngambil user 
    print("USER :" , selected_user ,"\n") 
    
    profile_form    = f.ProfileForm(    )
    
    if (request.method == 'POST' and profile_form.is_valid()):
        print('ok')
        if ( selected_user is not None):
            additional_data = profile_form.cleaned_data['additional_data']
            request.user.userprofile.additional_field = additional_data
            request.user.userprofile.save()
            user_profile = profile_form.save(commit=False)
            user_profile.save()
            selected_user.profile = user_profile


        return redirect('main:home',profile_form)
        
    context={
        "profile_form": profile_form
    }
    print(selected_user,"ini selected ")
    return render(request,"user_profile.html",context)

@csrf_exempt
def create_data_obat_ajax(request):
    

    if request.method == "POST":
        nama_obat = request.POST.get("nama_obat")
        amount = request.POST.get("stok")
        harga = request.POST.get("harga")
        satuan_harga = request.POST.get("jenis_satuan")
        jenis_obat = request.POST.get("jenis_obat")
        deskripsi = request.POST.get("deskripsi")
        expired = request.POST.get("expired")
        user = request.user

        new_obat = models.Item(nama_obat=nama_obat,amount=amount,harga=harga,satuan_harga=satuan_harga,jenis_obat = jenis_obat,deskripsi=deskripsi, expired=expired, user=user)
        new_obat.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
 
   
    