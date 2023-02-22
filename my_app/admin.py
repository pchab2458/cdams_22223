from django.contrib import admin
from .models import Room_type, Room, Extra, Billing, TenantProfile, MaintenanceService
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = (
        'bill_ref', 'room_no', 'tenant_name', 'bill_date', 'overdue_amount', 'late_fee', 'maint_cost', 'bill_total', 'payment_amount',
        'cf_amount',
        'status')
    list_filter = ('bill_ref', 'tenant_name', 'bill_date', 'status')
    search_fields = ('tenant_name', 'bill_ref')


#
# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     # pass # default
#     # add_form = CustomUserCreationForm # used by signup in the app
#     # form = CustomUserChangeForm
#     list_display = ['username', 'first_name', 'last_name', 'is_active', 'is_superuser']


@admin.register(TenantProfile)
class TenantProfileAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'room_no', 'phone', 'pin']


#
# @admin.register(MaintenanceCharge)
# class MaintenanceChargeAdmin(admin.ModelAdmin):
#     list_display = ['room_no', 'description', 'job_date', 'status']


@admin.register(MaintenanceService)
class MaintenanceServiceAdmin(admin.ModelAdmin):
    list_display = ['room_no', 'description', 'job_ref', 'job_date', 'job_cost']


@admin.register(Room_type)
class Room_typeAdmin(admin.ModelAdmin):
    list_display = ['description', 'rate']


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ['description', 'cpu']


# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ['room_no', 'room_type']
#     list_filter = ['room_type', ]


@admin.register(Room)
class Room_n(admin.ModelAdmin):
    list_display = ['room_no', 'room_type', 'status', 'exmovein_date']
    list_filter = ['room_type', 'status']
