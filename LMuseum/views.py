from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView
from django.forms import ModelForm
from django import forms
from LMuseum.forms import FeedbackForm




# Create your views here.
def HomePage(request):
    return render(request,'welcom_page.html')
def ExtendingPage(request):
    return render(request,'extending.html')
def BengalTiger(request):
    return render(request,'bengal_tiger.html')
def IndianElephant(request):
    return render(request,'indian_elephant.html')
def SnowLeopard(request):
    return render(request,'snow_leopard.html')
def AsiaticLion(request):
    return render(request,'asiatic_lion.html')
def RedPanda(request):
    return render(request,'red_panda.html')




def ExtinctPage(request):
    return render(request,'extinct.html')
def IndianAuroch(request):
    return render(request,'indian_auroch.html')
def IndianRhinoceros(request):
    return render(request,'indian_rhinoceros.html')
def HimalayanQuail(request):
    return render(request,'himalayan_quail.html')
def MalabarCivet(request):
    return render(request,'malabar_civet.html')
def PinkHeadedDuck(request):
    return render(request,'pink_headed_duck.html')
def RegisteredListPage(request):
    return render(request,"registered_list",{'post':post}) # type: ignore



def DonationPage(request):

    return render(request,'donation.html')




from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created. Please log in.')
        return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect
from django.contrib import messages
# feedback/views.py



from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Save to DB here
            return render(request, 'feed_back.html', {
                'form': FeedbackForm(),  # Empty form after submit
                'success': True
            })
    else:
        form = FeedbackForm()
    return render(request, 'feed_back.html', {'form': form})



