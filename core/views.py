from django.shortcuts import render
from django.http import HttpResponse
from .models import Fashion, Contact, Jewellery,Login,Home,Electronic
from phonenumbers import PhoneNumber, PhoneNumberFormat
from . import views
from django.contrib import admin
from .models import User
from .forms import MyForm
from django.http import HttpResponseRedirect



def index(request):
     contacts = Contact.objects.all()
     context = {
          'contacts' : contacts
     }
     return render(request, 'index.html', context)


# Create your views here.


def fashion(request):
     fashion = Fashion.objects.all()
     context = {
        'fashion' : fashion
     }
     return render(request, 'fashion.html', context)


def contact(request):
     contacts = Contact.objects.all()
     print(contacts)
     context = {
          'contacts' : contacts
     }
     return render(request, 'contact.html', context)


    # contacts = Contact.objects.all()
    # context = {
    #     'contacts': contacts,

def jewellery(request):
     jewellery = Jewellery.objects.all()
     context = {
          'jewellery' : jewellery
     }
     return render(request, 'jewellery.html', context)


def login(request):
     login = Login.objects.all()
     context = {
          'login' : jewellery
     }
     return render(request, 'login.html', context)


def home(request):
     home = Home.objects.all()
     context = {
          'home' : home
     }
     return render(request, 'index.html', context)


def electronic(request):
     electronic = Electronic.objects.all()
     context = {
          'electronic' :electronic
     }
     return render(request, 'electronic.html', context)



def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process form data
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})

