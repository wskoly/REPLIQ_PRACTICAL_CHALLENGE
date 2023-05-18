"""
URL configuration for REPLIQ_PRACTICAL_CHALLENGE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from tracker import views

router = routers.SimpleRouter()
router.register(r'companies', views.CompanyAPI)
router.register(r'company-staffs', views.CompanyStaffAPI)
router.register(r'company-Employee', views.CompanyEmployeeAPI)
router.register(r'assets', views.AssetAPI)
router.register(r'asset-allocation', views.AssetAllocationAPI)

#for API documentation
schema_view = get_schema_view(
   openapi.Info(
      title="API's for Asset allocation and tracking",
      default_version='v1',
      description="An demo project in completion of REPLIQ Jr. Django Practical Challenge ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #JWT API authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #API documentation
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + router.urls
