from rest_framework import viewsets
from . import models
from . import serializers

class  EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer = serializers.EmployeeSerializer

# list(), retrive(), create(), update(), destroy()