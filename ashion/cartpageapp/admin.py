from django.contrib import admin
from cartpageapp.models import cartpage_data
# Register your models here.
class cartpage_dataAdmin(admin.ModelAdmin):
    list_display = ('product_image','product_name','product_price')

admin.site.register(cartpage_data,cartpage_dataAdmin)


