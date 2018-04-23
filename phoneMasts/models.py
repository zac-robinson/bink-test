from django.db import models


class PhoneMasts(models.Model):
    property_name = models.CharField(max_length=150)
    property_address_1 = models.CharField(max_length=150)
    property_address_2 = models.CharField(max_length=150)
    property_address_3 = models.CharField(max_length=150)
    property_address_4 = models.CharField(max_length=150)
    unit_name = models.CharField(max_length=150)
    tenant_name = models.CharField(max_length=150)
    lease_start_date = models.CharField(max_length=25)
    lease_end_date = models.CharField(max_length=25)
    lease_years = models.IntegerField()
    current_rent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.property_name
