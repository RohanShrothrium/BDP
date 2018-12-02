from django.http import HttpResponse
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
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


# Create your views here.
def register(request):
	if request.user.is_authenticated:
		return redirect('blog-home')
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
				user = form.save(commit=False)
				user.is_active = False
				user.save()
				current_site = get_current_site(request)
				username = form.cleaned_data.get('username')
				print("before sending")
				#this is for sending email
				mail_subject = "Activate your BDP account"
				uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
				token = account_activation_token.make_token(user)
				message = render_to_string('users/acc_active_email.html', {'user': user,'domain': current_site.domain,'uid':uid,'token': token, })
				to_email = form.cleaned_data.get('email')
				email = EmailMessage(mail_subject, message, to=[to_email])
				email.send()
				print("after sending")
				return HttpResponse('Please confirm your email address to complete the registration')
	form = UserRegisterForm()
	context = {
		'count': count,
		'emailFlag': emailFlag,
		'form': form,
	}
	return render(request, 'users/register.html',context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


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

