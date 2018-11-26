from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	# This sets the time to when the post was posted but i have an option to change it when I want to
	date_posted = models.DateTimeField(default = timezone.now)
	event_date = models.DateTimeField(default = timezone.now)
	# on_delete ..... CASCADE deletes post when user is delted
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	venue = models.CharField(default = 'Dharwad', max_length = 50)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog-home')


class Enrolled(models.Model):
	user = models.IntegerField()
	event = models.IntegerField()

	def __str__(self):
		return str(self.user)