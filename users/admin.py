from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#
#     list_display = ['username','email',  'age', 'is_active','is_superuser']
#
#     model = CustomUser
#
#
# admin.site.register(CustomUser, CustomUserAdmin)

# ------------------------------------------------------------------

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # pass # default
    # add_form = CustomUserCreationForm # used by signup in the app
    # form = CustomUserChangeForm
    list_display = ['username', 'first_name', 'last_name', 'is_superuser']
    # list_display = ('username', 'email', 'first_name', 'last_name')  # [] or ()
