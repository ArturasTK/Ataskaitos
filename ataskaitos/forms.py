from django import forms
from django.forms import ModelForm
from .models import Product, Report, Remake, Reason  


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['date_field', 'dtk_nr', 'product_name', 'remakes', 'number_of_plates', 'number_of_new_plates', 'reasons', 'notes']
        exclude = ['user']
        # labels = {
        #     'date_field':''
        # #     'dtk_nr':
        # #     'product_name':
        # #     'remakes': 
        # #     'number_of_plates': 
        # #     'number_of_new_plates': 
        # #     'reasons': 
        # #     'notes': 
        # #     'user':
        # # }
        widgets = {
            'date_field': forms.DateTimeInput(attrs={'class':'form-control'}),
            'dtk_nr': forms.TextInput(attrs={'class':'form-control','placeholder': 'DTK'}),
            'product_name': forms.Select(attrs={'class':'form-control'}),
            'remakes': forms.Select(attrs={'class':'form-control'}),
            'number_of_plates': forms.NumberInput (attrs={'class':'form-control'}),
            'number_of_new_plates': forms.NumberInput (attrs={'class':'form-control'}),
            'reasons': forms.Select(attrs={'class':'form-control'}),
            'notes': forms.TextInput(attrs={'class':'form-control'}), 
            # 'user': forms.Select(attrs={'class':'form-control'}),
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'purpose': forms.TextInput(attrs={'class':'form-control'}),
        }

class RemakeForm(ModelForm):
    class Meta:
        model = Remake
        fields = '__all__'
        widgets = {
            'remakes': forms.TextInput(attrs={'class':'form-control'}),            
        }

class ReasonForm(ModelForm):
    class Meta:
        model = Reason
        fields = '__all__'
        widgets = {
            'reasons': forms.TextInput(attrs={'class':'form-control'}),            
        }