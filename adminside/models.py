from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

ORDERSTATUS = ((1, "Processed"), (2, "Dispatch"), (3, "En Route "), (4, "Delivered"))

class user (models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
    
class Order(models.Model):
    # sender information
    sender_name = models.CharField(max_length=50)
    sender_address = models.CharField(max_length=50)
    sender_email = models.EmailField()
    
    
    # Recievers information
    reciever_name = models.CharField(max_length=50, null=True, blank=True)
    Phone_number = models.CharField(null=True, blank=True, max_length=50)
    reciever_address = models.CharField(max_length=50, null=True, blank=True)
    reciever_email = models.EmailField()
   
    
    # Order information
    origin = models.CharField(max_length=50, null=True, blank=True)
    destination = models.CharField(max_length=50, null=True, blank=True)
    package = models.IntegerField(null=True)
    carrier = models.CharField(max_length=50, null=True, blank=True)
    type_of_shipment = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    reference_number = models.CharField(max_length=50, null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)
    departure_date = models.DateField(null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=True)
    departure_time = models.CharField(null=True, blank=True, max_length=10)
    arrival_time = models.CharField(null=True, blank=True,  max_length=10)
    payment_method = models.CharField(max_length=50, null=True, blank=True)  
    tracking_number = models.CharField(default=f"EXWA{str(uuid.uuid4())[:18]}-ORDER", max_length=30, unique=True)
    status = models.IntegerField(choices=ORDERSTATUS, default=1)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)
    date_added = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
        
        
    def generate_tracking_number(self):
        uuid_string = str(uuid.uuid4().int)
        formatted_uuid = f"EXWA{str(uuid.uuid4())[:18]}-ORDER"
        return formatted_uuid

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = self.generate_tracking_number()
        super().save(*args, **kwargs)
       
    

    
