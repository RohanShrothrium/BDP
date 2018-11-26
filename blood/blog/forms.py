from django import forms
from django.contrib.auth.models import User
from .models import Enrolled
from django.db import models

class EnrollForm(forms.ModelForm):
	class Meta:
		model = Enrolled
		fields = ['user', 'event',]

class EmergencyEmailForm(forms.Form):
	filtered_recipients = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'To filter recipients, search for something', 'rows': 3}), required=False)
	custom_recipients = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Add recipients...', 'rows':2}), required=False)
	subject = forms.CharField(max_length = 150)
	body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Let them know...', "rows": 8}), required=False)
