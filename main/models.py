from django.db import models
from django import forms
from datetime import datetime
from django.contrib.auth.models import User

dateNow = datetime.now()

#pengelolaan apotek
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #membuat pilihan (choice) untuk checkbox
    pilihan_jenis_obat ={
        ("Herbal/Suplemen","Herbal/Suplemen"),
        ("Alergi", "Alergi"),
        ("Generic","Generic"),
        ('Racik', "Racik"),
        ("Anak (0-17 tahun)","Khusus Anak (0-17 tahun)"),
        ("Penyakit Dalam","Penyakit dalam"),
        ("Lansia","Penyakit Orang Tua"),
        ("Ibadah","Obat Hati"),
        
    }
    
    
    pilihan_jenis_satuan_harga = {
        ("Strip","1 Strip"),
        ("Botol","Botol/Sirup"),
        ("Kotak/Kemasan","Kotak/Kemasan"),
        ("Kapsul","1 Butir Kapsul"),
        ("Sachete","Sachete"),
    }
    
    nama_obat = models.CharField(max_length=255) #nama obat
    amount = models.PositiveIntegerField() #stok obat tersedia
    harga = models.PositiveIntegerField() #harga per x
    satuan_harga = models.CharField(max_length=100,default="Kapsul",choices=pilihan_jenis_satuan_harga) #satuan harga per apa
    jenis_obat = models.CharField(max_length=100, default="Generic", choices=pilihan_jenis_obat) #jenis obat
    deskripsi = models.TextField()   #kegunaan obat
    expired = models.DateField(verbose_name="Expired \n(format : yyyy-mm-dd)") #expired
    
    
    

    def __str__(self):
        return "{}".format(self.nama_obat, self.amount, self.satuan_harga, self.jenis_obat,self.harga,self.deskripsi,self.expired)

class expired(forms.Form):
    expired = forms.DateField(
        widget=forms.SelectDateWidget)

    
    def __str__(self):
        return "{}".format(self.expired)



