from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from items.models import Category,Item
from.forms import SignupForm
from items.models import models
def index(request):
    item=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'index.html',{'categories':categories,'items':item})

def contact(request):
    return render(request,'contact.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()
               
        return redirect('/login')
    form = SignupForm()
    return render(request,'signup.html',{'form':form})

def login(request):
    return render(request,'login.html')