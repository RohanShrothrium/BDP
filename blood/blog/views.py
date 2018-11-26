from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post, Enrolled
from users.models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone
from datetime import *
from django.core.mail import send_mail
from django.conf import settings

def home(request):
	if request.user.is_authenticated:
		isEle = Eli(request.user)
		if request.method == 'POST':
			# here next...
			form = EnrollForm(request.POST)
			form.instance.user = request.user.id
			if form.is_valid():
				post = Post.objects.get(id = form.instance.event)
				temp = post.event_date.date()
				request.user.profile.last_donated = temp
				request.user.profile.save()
				form.save()
		else:		
			# we come here first and.....
			form = EnrollForm()
			form.instance.user = request.user.id


		context = {
			'posts': Post.objects.all().order_by("-date_posted"),
			'isHome': True,
			'form': form,
			'isEle': isEle>=112,
			'daysLeft': 112-isEle
		}
		return render(request, 'blog/home.html', context)
	else:
		context = { 
			'posts': Post.objects.all().order_by("-date_posted"),
		}
		return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'      #by default it is <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	

class PostCreateView(PermissionRequiredMixin, CreateView):
	permission_required = 'user.is_staff'
	model = Post
	fields = ['title', 'event_date', 'content', 'venue']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

def about(request):
	return render(request, 'blog/about.html')

def Eli(x):
	return (datetime.now().date() - x.profile.last_donated).days

def donors(request):
	form = EmergencyEmailForm()
	if request.method == 'POST':
		form = EmergencyEmailForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data.get("subject")
			filtered_recipients = form.cleaned_data.get("filtered_recipients")
			custom_recipients = form.cleaned_data.get("custom_recipients")
			body = form.cleaned_data.get("body")
			from_email = settings.EMAIL_HOST_USER
			all_recipients = filtered_recipients + custom_recipients
			to_list = all_recipients.split(",")
			send_mail(subject, body, from_email, to_list, fail_silently=False)
			success_mssg = "Your email has been sent successfully XD"
	else:
		success_mssg = ""
	people = User.objects.all()
	people = list(map(lambda x:[x,Eli(x)], people))
	context = {
		'people' : people,
		'form' : form,
		'message' : success_mssg
	}
	return render(request, 'blog/donors.html', context)

def ListEnrolled(request):
	people = User.objects.all()
	posts = Post.objects.all()
	enrolled = Enrolled.objects.all()
	context = {
		'people' : people,
		'posts' : posts,
		'enrolled' : enrolled,
	}
	return render(request, 'blog/list.html', context)