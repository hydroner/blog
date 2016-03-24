from django.shortcuts import render, redirect

# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import PostForm, LoginForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


@login_required()
def edit(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['post']
            user = request.user
            date = datetime.now()
            p = Post(title=title, content=content, user=user,date=date)
            p.save()
            return redirect('index')
    else:
        form = PostForm()
        print request.user
    return render(request, 'blog/edit.html', {'form': form})


def loginto(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print password
        print username
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('edit')
        else:
            return HttpResponse('Invalid user')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})
              
def logout(request):
    pass

def register(request):
    pass

