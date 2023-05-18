from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

class CompanyAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    
class CompanyStaffAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyStaffSerializer
    queryset = CompanyStaff.objects.all()


class CompanyEmployeeAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyEmployeeSerializer
    queryset = CompanyEmployee.objects.all()
    
class AssetAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()

class AssetAllocationAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AssetAllocationSerializer
    queryset = AssetAllocation.objects.all()