from django.forms import ModelForm
from .models import Quote
        
class Messageform(ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'
        
class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'