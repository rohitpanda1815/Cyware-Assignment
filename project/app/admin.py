from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display=('username','first_name','email','date_joined')
    list_filter=['email','date_joined']
admin.site.register(User,UserAdmin)
