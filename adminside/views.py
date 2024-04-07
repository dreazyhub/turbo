from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import Orderform, Userform
from . models import Order
from clientside.models import Quote
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.

@login_required
def Dashboard(request):
    count =Order.objects.count()
    return render(request, 'index.html', {'count':count} )

# def logoutUser(request):
#     logout(request)
#     return redirect('panel_admin:login')


def loginUser(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('username does not exist')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('AdminSide:dashboard')   
        else:
            print('Username or password is not correct')         
    return render(request, 'login.html')


def NewOrder(request):
    form = Orderform()  
    if request.method =='POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminSide:order-list')
    context = {'form':form}
    return render(request, 'newOrder.html',context )

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
    
    if request.method == 'POST':
        form = Orderform(request.POST, instance=order)
        
        if form.is_valid():
            form.save()

            # Determine the status of the order
            status = order.status  

            # Select email template based on status
            if status in ['Processed', 'Dispatch', 'En Route', 'Delivered']:
                email_template = 'email_template.html'  # Change this to the appropriate email template for each status

                # Render email template with order details
                email_context = {'order': order}
                email_content = render_to_string(email_template, email_context)

                # Send HTML email
                email_subject = 'Order status updated'
                sender_email = 'Tzuarg@gmail.com'  # Update with your email
                recipient_email = order.email  # Assuming 'email' is a field in your Order model
                email = EmailMessage(email_subject, email_content, sender_email, [recipient_email])
                email.content_subtype = 'html'
                email.send()

            return redirect('AdminSide:order-list')
    
    context = {'form': form}
    return render(request, 'newOrder.html', context)


def OrderList(request):
    orders = Order.objects.all()
    return render(request, 'orderList.html', {'orders': orders})

def details(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'details.html', {'order': order})

def deleteorder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method =='POST':
        order.delete()
        return redirect('AdminSide:order-list')
    context = {'order': order}
    return render(request, 'delete.html', context)

  
def Allmessages(request):
    messages = Quote.objects.all()
    return render(request, 'allmessages.html', {'messages': messages})

def messageDetails(request, pk):
    messages = Quote.objects.get(id=pk)
    return render(request, 'messageDetail.html', {'messages':messages})

def deletemessage(request, pk):
    message = Quote.objects.get(id=pk)
    if request.method =='POST':
        message.delete()
        return redirect('AdminSide:allmessages')
    context = {'message': message}
    return render(request, 'delete.html', context)


def status(request):
    return render(request, 'email_template.html')