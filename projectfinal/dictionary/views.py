from django.shortcuts import render

from dictionary.forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index',))
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                new_user = User.objects.create_user(**form.cleaned_data)
                login(request,new_user)
                # redirect, or however you want to get to the main view
                return HttpResponseRedirect(reverse('index',))
        else:
            form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)
