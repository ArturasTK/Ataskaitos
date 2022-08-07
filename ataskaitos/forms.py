from pyexpat import model
from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('date_field', 'dtk_nr', 'product_name', 'remakes', 'number_of_plates', 'number_of_new_plates', 'reasons', 'notes', 'user')
        # labels = {
        #     'date_field':
        #     'dtk_nr':
        #     'product_name':
        #     'remakes': 
        #     'number_of_plates': 
        #     'number_of_new_plates': 
        #     'reasons': 
        #     'notes': 
        #     'user':
        # }
        widgets = {
            'date_field': forms.DateInput(attrs={'class':'form-control','id':'inlineFormInputDate'}),
            'dtk_nr': forms.TextInput(attrs={'class':'form-control','id':'inlineFormTextDate'}),
            'product_name': forms.Select(attrs={'class':'form-control'}),
            'remakes': forms.Select(attrs={'class':'form-control'}),
            'number_of_plates': forms.NumberInput (attrs={'class':'form-control'}),
            'number_of_new_plates': forms.NumberInput (attrs={'class':'form-control'}),
            'reasons': forms.Select(attrs={'class':'form-control'}),
            'notes': forms.TextInput(attrs={'class':'form-control'}), 
            'user': forms.Select(attrs={'class':'form-control'}),
        }
