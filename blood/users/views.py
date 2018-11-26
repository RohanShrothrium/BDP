from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, ProfileCreateForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import *
import functools as ft
# these were added for email-verification
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def register(request):
	emailFlag = False
	count = 0
	tempUser = ''
	email = ''
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			count = User.objects.all().filter(email = str(form.instance.email)).count()
			if count > 0:
				emailFlag = True
			else:
				form.save()
				username = form.cleaned_data.get('username')

				#this is for sending email
				sentences=[
					"Dear ", str(username), 
					",\n\tWelcome to IIT Dharwad's Blood Donation Portal. ",
				    "We really appreciate your initiative to donate blood. ",
				    "We look forward to see you take part in our blood donation camps."
				    "\n\nYours faithfully",
				    "\nIITDh BDP Team\n"
				]
				subject = "Thank you for signing up at the Blood Donation Portal"
				ddklal = ft.reduce(lambda x,y: x+y, sentences)
				from_email = settings.EMAIL_HOST_USER
				to_list = [form.cleaned_data.get('email')]
				send_mail(subject, ddklal, from_email, to_list, fail_silently=False)
				#email is sent

				messages.success(request, f'Account created for {username}!')
				return redirect('login')
	form = UserRegisterForm()
	context = {
		'count': count,
		'emailFlag': emailFlag,
		'form': form,
	}
	return render(request, 'users/register.html',context)

@login_required
def profile(request):
	if request.method == 'POST':
		p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
		if request.user.profile.is_registered == False:
			pc_form = ProfileCreateForm(request.POST, instance=request.user.profile)
			if p_form.is_valid() and pc_form.is_valid():
				p_form.save()
				pc_form.save()
		else:
			if p_form.is_valid():
				p_form.save()
		return redirect('profile')

	else: 
		p_form = ProfileUpdateForm(instance=request.user.profile)
		pc_form = ProfileCreateForm(instance=request.user.profile)
		days = (datetime.now().date() - request.user.profile.last_donated).days
		isEli = days >= 112
		left = 112 - days
		context = {
			'p_form': p_form,
			'pc_form': pc_form,
			'days': days,
			'isEli': isEli,
			'left' : left
		}
		return render(request, 'users/profile.html', context)

