from django.db import models
import uuid

# Create your models here.

class Client(models.Model):
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField()
    subject = models.CharField(max_length = 50)
    message = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.sender_name
    
class Quote(models.Model):
    departure = models.CharField(max_length= 50, null = True)
    delivery = models.CharField(max_length= 50, null = True)
    weight = models.CharField(max_length= 50, null = True)
    dimensions = models.CharField(max_length= 50, null = True)
    name = models.CharField(max_length=50, null = True)
    email = models.EmailField( null = True)
    phone = models.CharField(max_length = 50, null = True)
    message = models.TextField(max_length = 200, null = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)
    
    def __str__(self):
        return self.name
    