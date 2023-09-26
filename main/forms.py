from django.forms import ModelForm
from . import models
from django import forms


class ProductForms(ModelForm):
    class Meta:
        model = models.Item
        fields = ["nama_obat", "amount", "harga", "satuan_harga","jenis_obat","expired", "deskripsi"]
        

class ExpiredForms(forms.ModelForm):
    class Meta:
        model = models.Item
        fields =['expired']
        

    
expired = forms.DateField(
    widget=forms.DateInput(
        attrs={
            
            'class': 'form-control',
            'type':"date",
        }
    )
)

class DateInput(forms.DateInput):
    input_type = 'date'
    

