from django.db import models
from django import forms
from datetime import datetime

dateNow = datetime.now()
#pengelolaan apotek
class Item(models.Model):
    
    pilihan_jenis_obat ={
        ("h","Herbal/Suplemen"),
        ("a", "Alergi"),
        ("g","Generic"),
        ('r', "Racik"),
        ("An","Khusus Anak (0-17 tahun)"),
        ("pd","Penyakit dalam"),
        ("ot","Penyakit Orang Tua"),
        
    }
    pilihan_jenis_satuan_harga = {
        ("s","1 Strip"),
        ("b","Botol/Sirup"),
        ("k","Kotak/Kemasan"),
        ("c","1 Butir Kapsul"),
    }
    
    nama_obat = models.CharField(max_length=255) #nama obat
    amount = models.IntegerField() #stok obat tersedia
    harga = models.PositiveIntegerField() #harga per x
    satuan_harga = models.CharField(max_length=100,default="Kapsul",choices=pilihan_jenis_satuan_harga) #satuan harga per apa
    jenis_obat = models.CharField(max_length=100, default="Generic", choices=pilihan_jenis_obat) #jenis obat
    deskripsi = models.TextField()   #kegunaan obat
    expired = models.CharField( max_length=8,default=dateNow.strftime("%a %d %B %Y")) #expired
    
    
    

    def __str__(self):
        return "{}".format(self.nama_obat, self.amount, self.satuan_harga, self.jenis_obat,self.harga, self.satuan_harga,self.deskripsi)

# class date(forms.Form):
#     expired = models.DateField(auto_now=True,default=datetime.now()) #expired
#     def __str__(self):
#         return "{}".format(self.expired)

    

