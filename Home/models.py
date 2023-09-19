from django.db import models

class data_pengguna(models.Model):
    nama_pengguna = models.CharField( max_length=50)
    email_pengguna =  models.EmailField( max_length=254)
    pass_pengguna = models.CharField(max_length=8)
    
    def __str__(self):
            return "{}".format(self.nama_pengguna,self.email_pengguna,self.pass_pengguna)

class riwayat_pengguna(models.Model):
    
    yes_or_no = {("Y","Ya"), ("N","Tidak")}
    
    penyakit =  models.CharField(max_length=500)
    usia = models.PositiveIntegerField(("Usia"))
    penyakit_genetik =  models.CharField(max_length=5, choices=yes_or_no)
    
    def __str__(self):
         return "{}".format(self.penyakit,self.usia,self.penyakit_genetik)
        
    


    