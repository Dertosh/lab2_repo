from django.contrib import admin


# Register your models here.
from myApp.models import UserShop


class UserShopAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login')
    fields = ['username', 'first_name', 'last_name',
              'email', 'last_login',
              'is_staff', 'is_active', 'date_joined',
              ]
    search_fields = ['username']
    list_filter = ['date_joined']


admin.site.register(UserShop, UserShopAdmin)
