from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
    
@admin.register(CompanyStaff)
class CompanyStaffAdmin(admin.ModelAdmin):
    list_filter = ('company',)
    
@admin.register(CompanyEmployee)
class CompanyEmployeeAdmin(admin.ModelAdmin):
    list_filter = ('company',)
    
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_filter = ('company',)
    
@admin.register(AssetAllocation)
class AssetAllocationAdmin(admin.ModelAdmin):
    list_filter = ('asset','employee','checkout_date', 'return_date', 'allocated_by')