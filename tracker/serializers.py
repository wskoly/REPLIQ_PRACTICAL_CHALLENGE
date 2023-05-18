from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        
class CompanyStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStaff
        fields = "__all__"
        
class CompanyEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyEmployee
        fields = "__all__"
        
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"
        
class AssetAllocationSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        #to validate if the asset already occupied by someone
        if (not attrs['asset'].is_available) and (attrs['return_date']== None):
            raise serializers.ValidationError("Asset is occupied.")
        
        # to validate if the allocator, the asset and the employee belongs to the same company
        if not ((attrs['allocated_by'].company == attrs['asset'].company) and (attrs['asset'].company == attrs['employee'].company)):
            raise serializers.ValidationError("Employee, Staff, and Asset must belong to the same company")
        return super().validate(attrs)
    
    def save(self, **kwargs):
        #toggling the asset availability on checked out and returned in as per the value of the return_date
        if self.validated_data['return_date']:
            self.validated_data['asset'].is_available = True
        else:
            self.validated_data['asset'].is_available = False
        self.validated_data['asset'].save()
        return super().save(**kwargs)
    
    class Meta:
        model = AssetAllocation
        fields = "__all__"