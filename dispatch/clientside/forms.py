from django.forms import ModelForm
from .models import Client, Quote, Message


class Contactform(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        
class Messageform(ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'