from django.forms import ModelForm
from .models import Order, user



class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
        
class Userform(ModelForm):
    class Meta:
        model = user
        fields = '__all__'