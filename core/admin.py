from django.contrib import admin
from .models import Mascota, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion', 'Mascota']
    search_fields = ['nombre', 'precio']
    list_filter = ['Mascota']
    list_per_page = 10


admin.site.register(Mascota)
admin.site.register(Producto, ProductoAdmin)
