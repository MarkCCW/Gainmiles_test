from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    sex = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "employee"
