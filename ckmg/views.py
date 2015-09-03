from django.shortcuts import render, get_object_or_404, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from ckmg.models import *
# Create your views here.

def index(request):
	return render(request, 'ckmg/index.html')

def header_info(request):
	return render(request, 'ckmg/header.html')

def footer_info(request):
	return render(request, 'ckmg/footer.html')

def aboutus_info(request):
	return render(request, 'ckmg/aboutus.html')

def theorynotes_info(request):
	return render(request, 'ckmg/theorynotes.html')

def modelpapers_info(request):
	return render(request, 'ckmg/modelpapers.html')

def ppt_info(request):
	return render(request, 'ckmg/ppt.html')

def project_info(request):
	return render(request, 'ckmg/projects.html')

def businessplan_info(request):
	return render(request, 'ckmg/businessplan.html')

def service_info(request):
	return render(request, 'ckmg/services.html')

def training_info(request):
	return render(request, 'ckmg/training.html')

def guidance_info(request):
	return render(request, 'ckmg/guidance.html')

def contact_info(request):
	return render(request, 'ckmg/contactus.html')
