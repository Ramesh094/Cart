from django.shortcuts import render, redirect
from items.models import Category, Item
from .forms import SignUpForm

from django.contrib.auth import logout
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all

    return render(request, 'html/index.html', context={
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'html/contact.html')


def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'html/signup.html', {
        'form': form
    })   

def user_logout(request):
    logout(request)
    return redirect('html/login.html')