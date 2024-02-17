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
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField()
    subject = models.CharField(max_length = 50)
    message = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.sender_name
    
class Message(models.Model):
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField()
    subject = models.CharField(max_length = 50)
    message = models.CharField(max_length = 200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)

    def __str__(self):
        return self.sender_name
    
    