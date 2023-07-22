from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from company.views import EmployeeViewSet, DepartmentListAPIView

app_name = 'company'

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')

urlpatterns = [
    path('departments/', DepartmentListAPIView.as_view(), name='departments'),
]

urlpatterns += router.urls

# urlpatterns = [
#     path('', include(api)),
# ]
