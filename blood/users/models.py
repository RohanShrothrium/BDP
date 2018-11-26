from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
	Male = 'MALE'
	Female = 'FEMALE'
	A1 = 'A+'
	A2 = 'A-'
	B1 = 'B+'
	B2 = 'B-'
	O1 = 'O+'
	O2 = 'O-'
	AB1 = 'AB+'
	AB2 = 'AB-'
	gender_choice = ((Male, 'MALE'), (Female, 'FEMALE'),)
	blood_choice = ((A1, 'A+ve'), (A2, 'A-ve'), (B1, 'B+ve'), (B2, 'B-ve'), (O1, 'O+ve'), (O2, 'O-ve'), (AB1, 'AB+ve'), (AB2, 'AB-ve'),)
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	#image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
	last_donated = models.DateField(default = timezone.now)
	about = models.TextField(default = 'Hey There!')
	mobile_number = models.CharField(max_length = 14, default = '0836 2212842')
	weight = models.CharField(max_length = 3, default = '69')
	roll_number = models.CharField(max_length = 10, default = 'NA')
	blood_group = models.CharField(max_length = 5, default = A1, choices = blood_choice)
	date_of_birth = models.DateField(default = timezone.now)
	gender = models.CharField(max_length = 10, default = Male, choices = gender_choice)
	is_registered = models.BooleanField(default = False)


	def __str__(self):
		return f'{self.user.username} Profile'