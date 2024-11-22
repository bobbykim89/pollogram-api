from django.contrib import admin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'username')
    list_display = ('email', 'username')


admin.site.register(CustomUser, CustomUserAdmin)
