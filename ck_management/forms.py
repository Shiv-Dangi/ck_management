from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	"""docstring for MyregisterationForm"""
	def __init__(self, arg):
		super(MyregisterationForm, self).__init__()
		self.arg = arg
