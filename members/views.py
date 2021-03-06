from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
	form_class = UserCreationForm
	template_name = 'members/register.html'
	success_url=reverse_lazy('login')

class UserLoginView(generic.CreateView):
	form_class = UserCreationForm
	template_name = 'members/login.html'
	success_url=reverse_lazy('login')
# Create your views here.
