from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('date_field', 'dtk_nr', 'product_name', 'remakes', 'number_of_plates', 'number_of_new_plates', 'reasons', 'notes')
