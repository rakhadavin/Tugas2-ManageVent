from django.forms import ModelForm
from . import models
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class ProductForms(ModelForm):
    class Meta:
        model = models.Item
        fields = ["nama_obat", "amount", "harga", "satuan_harga","jenis_obat","expired", "deskripsi","gambar"]

    expired = forms.DateField(widget=DateInput)
   
   
class profileForm(ModelForm):
    class Meta:
        model = models.user_profile
        fields=["user","profile_picture", "nama_profile","user_email"]
    
    

        

