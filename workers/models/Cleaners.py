# services/models.py
from django.db import models
from .baseModel import BaseModel
from .Services import Category, Service
from authentication.models.models import CustomUser
# from django.contrib.gis.geos import Point
# from location_field.models.spatial import LocationField

class Cleaner(BaseModel):
    name = models.CharField(max_length=255)
    about = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    # location = LocationField(based_fields=['city','address'], zoom=7, default=Point(1.0, 1.0))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    services = models.ManyToManyField(Service)
    contactPerson = models.CharField(max_length=255)
    email = models.EmailField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name