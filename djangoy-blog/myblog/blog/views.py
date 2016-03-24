from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import PostForm, LoginForm
from .models import Post, Author


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


@login_required(login_url='/blog/login/')
def edit(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            user = request.user
            p = Post(title=title, post=post, user=user)
            p.save()
            return redirect('index')
    else:
        form = PostForm()
    return redirect('login')
                

def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Author.objects.filter(username__exact=username,
                                         password__exact=password)
            if user:
                edit_form = PostForm()
                response = render(request, 'blog/edit.html', {'form': edit_form})
                return response
            else:
                return HttpResponseRedirect('/blog/login/')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})
                
def logout(request):
    pass

def register(request):
    pass

