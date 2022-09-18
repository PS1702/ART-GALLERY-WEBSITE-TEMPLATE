from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home.html')
    # return HttpResponse("This is homepage.")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About page.")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        messages.success(request, 'Your message has been sent')
        contact.save()
    
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact page.")

def abstract(request):
    return render(request, 'abstract.html')

def sketches(request):
    return render(request, 'sketches.html')

def digital(request):
    return render(request, 'digital.html')

def handmade(request):
    return render(request, 'handmade.html')