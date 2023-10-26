from django.contrib import admin
from exapp.models import Producttab

# Register your models here.
class ProducttabAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'pname', 'price','stock', 'description')
admin.site.register(Producttab, ProducttabAdmin)