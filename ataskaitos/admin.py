from django.contrib import admin
from .models import Product, Report, Remake, Reason

admin.site.register(Product)

admin.site.register(Remake)

admin.site.register(Reason)

admin.site.register(Report)
