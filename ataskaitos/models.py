from audioop import ratecv
from django.db import models
from datetime import date

class Product(models.Model):
    product_name = models.CharField('Produktas', max_length=50)
    price = models.DecimalField('Įkainis', max_digits=10, decimal_places=2) 

    def __str__(self):
       return str(self.product_name) + ": €" + str(self.price)


class Remake(models.Model):
    remakes = models.CharField('Perdarymai', max_length=50)

    def __str__(self):
        return str(self.remakes)


class Reason(models.Model):
    reasons = models.CharField('Priežastys', max_length=50)

    def __str__(self):
        return str(self.reasons)


class Report(models.Model):
    date_field = models.DateField('Data', default=date.today)
    dtk_nr = models.CharField('DTK Nr.', max_length=10)
    product_name = models.ForeignKey(Product, help_text='Pasirinkite produktą', on_delete=models.SET_NULL, null=True)
    remakes = models.ForeignKey(Remake, help_text='Pasirinkite perdarimo priežastis', on_delete=models.SET_NULL, null=True)
    # number_of_plates =
    # number_of_new_plates = 
    # price = ?
    # total = 
    reasons = models.ForeignKey(Reason, help_text='Pasirinkite korekcijos tipą', on_delete=models.SET_NULL, null=True)
    notes = models.TextField('Pastabos', max_length=1000, help_text='Papildomi dabai')
    def __str__(self):
        return f'{self.date_field} {self.dtk_nr}'




