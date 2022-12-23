from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    views['service'] = Service.objects.all()
    return render(request, 'index.html', views)

def about(request):
    return render(request, 'about.html')

def contact(request):
    views = {}
    views['infos'] = Information.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            )
        data.save()
        views['mess'] = 'The message is Submitted'
        return render(request, 'contact.html', views)

    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def price(request):
    return render(request, 'price.html')

def services(request):
    return render(request, 'services.html')

