from api.models import Employee
from api.serializers import EmployeeSerializer

from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
