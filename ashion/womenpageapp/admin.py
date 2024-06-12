from django.contrib import admin

from womenpageapp.models import women_poster_carousel ,women_poster_offer ,women_product_collection ,women_product_carousel ,women_bottom_poster

# Register your models here.
class women_poster_carouselAdmin (admin.ModelAdmin):
    list_display = ('poster_img',)

admin.site.register(women_poster_carousel, women_poster_carouselAdmin)


class women_poster_offerAdmin (admin.ModelAdmin):
    list_display = ('offer_img',)

admin.site.register(women_poster_offer, women_poster_offerAdmin)


class women_product_carouselAdmin (admin.ModelAdmin):
    list_display = ('product_img','product_title','product_des','product_price',)

admin.site.register(women_product_carousel, women_product_carouselAdmin)


class women_product_collectionAdmin (admin.ModelAdmin):
    list_display = ('product_img','product_title','product_des','product_price',)

admin.site.register(women_product_collection, women_product_collectionAdmin)


class women_bottom_posterAdmin (admin.ModelAdmin):
    list_display = ['bottom_img',]

admin.site.register(women_bottom_poster, women_bottom_posterAdmin)
