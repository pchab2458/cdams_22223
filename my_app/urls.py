from django.urls import path
from . import views

urlpatterns = [

    path('admin_page/', views.admin_page, name='admin_page'),
    path('', views.gateway, name='gateway'),  # one only ... blank ('')
    path('create_contract/', views.create_contract, name='create_contract'),
    path('billing/', views.billing, name='billing'),
    path('month_bills/', views.month_bills, name='month_bills'),
    path('pay_bill/<str:bref>/', views.pay_bill, name='pay_bill'),
    path('report_type/', views.report_type, name='report_type'),
    path('report_parameters/', views.report_parameters, name='report_parameters'),
    path('extra_rates/', views.extra_rates, name='extra_rates'),
    path('elec_cpu_change/', views.elec_cpu_change, name='elec_cpu_change'),
    path('water_cpu_change/', views.water_cpu_change, name='water_cpu_change'),
    path('room_type_rate/', views.room_type_rate, name='room_type_rate'),
    path('current_tenants/', views.current_tenants, name='current_tenants'),
    path('vacant_rooms/', views.vacant_rooms, name='vacant_rooms'),
    path('update_room_status/<str:rmn>/', views.update_room_status, name='update_room_status'),
    path('monthly_report/', views.monthly_report, name='monthly_report'),
    path('misc_contents/', views.misc_contents, name='misc_contents'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('user_list_to_delete/', views.user_list_to_delete, name='user_list_to_delete'),
    path('delete_user/<str:rmn>/', views.delete_user, name='delete_user'),
    path('confirm_delete_user/<str:k>/', views.confirm_delete_user, name='confirm_delete_user'),
    path('register/', views.Register.as_view(), name='register'),
    path('register/done/', views.register_done, name='register_done'),
    path('change_password/', views.change_password, name='change_password'),
    path('maintenance_charge/', views.maintenance_charge, name='maintenance_charge'),
    path('new_tenant/', views.new_tenant, name='new_tenant'),
    path('tenant_profile/', views.tenant_profile, name='tenant_profile'),
    path('tenant_bill/', views.tenant_bill, name='tenant_bill'),
    path('tenant_info/', views.tenant_info, name='tenant_info'),

    path('pre_create_new_account', views.pre_create_new_account_excel, name='pre_create_new_account'),
    path('create_new_account_excel', views.create_new_account_excel, name='create_new_account_excel'),

    path('issue_bill_excel', views.issue_bill_excel, name= 'issue_bill_excel'),

]
