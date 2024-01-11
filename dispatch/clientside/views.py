from django.shortcuts import render
from adminside.models import Order
from django.contrib import messages

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Services(request):
    return render(request, 'services.html')

def Track(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        try:
            model_instance = Order.objects.get(tracking_number=tracking_number)
            return render(request, 'track.html', {'model_instance': model_instance})
        except Order.DoesNotExist:
            messages.error(request, 'Order not found.')
    return render(request, 'track.html')


def Contact(request):
    return render(request, 'contact.html')

def Quote(request):
    return render(request, 'get-a-quote.html')

