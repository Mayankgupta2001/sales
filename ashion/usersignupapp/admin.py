from django.contrib import admin
from usersignupapp.models import user_signup_data
# Register your models here.
class user_signup_dataAdmin(admin.ModelAdmin):
    list_display = ('name','email','password')

admin.site.register(user_signup_data,user_signup_dataAdmin)