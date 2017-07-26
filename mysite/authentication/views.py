from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Create your views here.

def index(request):
	return render(request, 'authentication/index.html')

def register_user(request):
	if request.method=='POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			email = userObj['email']
			password = userObj['password']

			if not(User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				User.objects.create_user(username, email, password)
				user = authenticate(username = username, password = password)
				login(request, user)
				return redirect('authentication:home')
			else:
				raise forms.ValidationError('Username with that email or password already exists')

	else:
		form = UserRegistrationForm()
	return render(request, 'authentication/register-user.html', {'form' : form})

