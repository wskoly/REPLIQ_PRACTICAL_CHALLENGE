from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    
class CompanyStaff(models.Model):
    company = models.ForeignKey(Company, related_name="company_staff", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.company}"
    
    class Meta:
        verbose_name = 'Company Staff'
        verbose_name_plural = 'Company Staffs'
        
class CompanyEmployee(models.Model):
    company = models.ForeignKey(Company, related_name="company_employee", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.company}"
    
    class Meta:
        verbose_name = 'Company Employee'
        verbose_name_plural = 'Company Employees'
        
class Asset(models.Model):
    company = models.ForeignKey(Company, related_name="company_asset", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    identification_number = models.CharField(max_length=200)
    is_available =  models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.company}"
    
    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'
        
class AssetAllocation(models.Model):
    asset = models.ForeignKey(Asset, related_name="allocated_asset", on_delete=models.PROTECT)
    employee = models.ForeignKey(CompanyEmployee, related_name="allocated_employee", on_delete=models.PROTECT)
    checkout_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(blank=True, null=True)
    checkout_condition = models.TextField(blank=True, null=True)
    return_condition = models.TextField(blank=True, null=True)
    allocated_by = models.ForeignKey(CompanyStaff, related_name="allocated_by", blank=True, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f"{self.asset.name} - {self.employee}"
    
    class Meta:
        verbose_name = 'Asset Allocation'
        verbose_name_plural = 'Asset Allocations'

