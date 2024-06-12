from django.contrib import admin
from menpageapp.models import men_poster_carousel ,men_poster_offer ,men_product_carousel ,men_product_collection ,men_bottom_poster

# Register your models here.
class men_poster_carouselAdmin (admin.ModelAdmin):
    list_display = ('poster_img',)

admin.site.register(men_poster_carousel, men_poster_carouselAdmin)


class men_poster_offerAdmin (admin.ModelAdmin):
    list_display = ('offer_img',)

admin.site.register(men_poster_offer, men_poster_offerAdmin)


class men_product_carouselAdmin (admin.ModelAdmin):
    list_display = ('product_img','product_title','product_des','product_price',)

admin.site.register(men_product_carousel, men_product_carouselAdmin)


class men_product_collectionAdmin (admin.ModelAdmin):
    list_display = ('product_img','product_title','product_des','product_price',)

admin.site.register(men_product_collection, men_product_collectionAdmin)


class men_bottom_posterAdmin (admin.ModelAdmin):
    list_display = ['bottom_img',]

admin.site.register(men_bottom_poster, men_bottom_posterAdmin)