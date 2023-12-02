from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from .models import Ads
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1'] 
        user = authenticate(request,username = username,password = pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            return redirect('index')
    return render(request, 'login.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']    
        pass2 = request.POST['pass2'] 
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request,"your aconta seccsees")
        return render(request, 'login.html')
    
    return render(request, 'signin.html')

def profile(request):
    user_id = request.user.id
    ads = Ads.objects.filter(user=user_id)
    
    return render(request , 'profile.html',{'user':request.user,'user_ads':ads})

def add_ads(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ad = Ads(user=request.user,title=title,description=description)
        ad.save()
        return redirect('post_list')
    return render(request,'add_ads.html')

def post_list(request):
    ad = Ads.objects.all()
    return render(request,'post_list.html',{'ads':ad})

def update_ad(request,id):
    ad = Ads.objects.get(id=id)
    if request.method == 'POST':
        ad.title = request.POST['title']
        ad.description = request.POST['description']
        ad.save()
        return redirect('index')
    return render(request,'update_ad.html',{'ad' : ad})

def delete_ad(request,id):
    ad = Ads.objects.get(id = id)
    if request.method == 'POST':
        ad.delete()
        return redirect('index')
    return render(request, 'delete_ad.html',{'ad' : ad})


def detile(request,id):
    ad_id = Ads.objects.get(id=id)
    return render(request,'detile.html',{'ad_id':ad_id})