from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def main_home(request):
    if request.method == "POST":
        u = request.POST['username']
        try:
            user = User.objects.get(username=u)
            return redirect('user_post', user.id)
        except:
            messages.info(request,'This is not Valid Username try another...')
            return redirect('blog_page')
    return render(request,'blog_page.html')

def blog_page(request):
    post = Post.objects.filter(user=request.user)
    d = {'post':post}
    return render(request,'my_blog.html',d)

def user_post(request,pid):
    user = User.objects.get(id=pid)
    post = Post.objects.filter(user=user,mode="public")
    d = {'post':post,'user':user}
    return render(request,'user_post.html',d)

def add_post(request):
    if request.method == "POST":
        t = request.POST['title']
        i = request.FILES['file']
        d = request.POST['desc']
        m = request.POST['mode']
        post = Post.objects.create(user=request.user,title=t,image=i,description=d,mode=m)
        messages.success(request,'Send Post Successfully')
        return redirect('blog_page')
    return render(request,'add_post.html')

def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Submit")
            return redirect('login')
    else:
        form = UserCreationForm()
    d = {'form': form}
    return render(request, 'register.html', d)

def Login(request):
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            messages.success(request,'Logged In Successfully')
            return redirect('blog_page')
        else:
            messages.success(request, 'Invalid Credentials')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    messages.success(request,'You have Logged Out')
    return redirect('login')
