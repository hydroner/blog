from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PostForm, LoginForm


def index(request):
    return render(request, 'index.html', {'form': form})


def edit(request):
    pass


def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Author.objects.filter(usernmae__=username,
                                         password__exact=password)
            if user:
                response = HttpResponseRedirect('/blog/')
                return response
            else:
                return HttpResponseRedirect('/blog/login/')
    else:
        form = LoginForm()
    return render_to_response('blog/login.html', {'form': form})
                
def logout(request):
    pass

def register(request):
    pass

