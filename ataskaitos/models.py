from audioop import ratecv
from django.db import models

class Product(models.Model):
    product_name = models.CharField('Produktas', max_length=50)
    price = models.DecimalField('Įkainis', max_digits=10, decimal_places=2) 

    def __str__(self):
       return str(self.item) + ": $" + str(self.price)

    

# class Report(models.Model):
#     date_field =
#     dtk_nr =
#     product_name = 
#     remakes =
#     number_of_plates =
#     number_of_new_plates = 
#     price = 
#     total = 
#     reasons =
#     notes = 





