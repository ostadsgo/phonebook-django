from django.db import models


class Contact(models.Model):
    employee_name = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    city = models.CharField(max_length=50)
    org_position = models.CharField(max_length=128)
    interal_phone =  models.CharField(max_length=5)
    phone =  models.CharField(max_length=20)

    def __str__(self):
        return f"{self.employee_name} - {self.org_position}"
