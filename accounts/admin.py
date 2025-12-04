from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display=('email','username','is_staff','is_active','is_superuser')
    fieldsets = (
        (None,{'fields':('email','username','password','is_staff','is_active','is_superuser','date_joined')}),
    )


admin.site.register(User,CustomUserAdmin)
