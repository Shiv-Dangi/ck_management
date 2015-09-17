from django.shortcuts import render, get_object_or_404, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from ckmg.models import *
# Create your views here.

def index(request):
	mrnews_list = news.objects.all().filter(news_type="MN")
	hrnews_list = news.objects.all().filter(news_type="HRN")
	fanews_list = news.objects.all().filter(news_type="FN")
	conews_list = news.objects.all().filter(news_type="CO")
	advertisements = advertise.objects.all()
	context = {'mrnews_list':mrnews_list, 'hrnews_list':hrnews_list, 'fanews_list':fanews_list, 'conews_list':conews_list, 'advertisements':advertisements}
	return render(request, 'ckmg/index.html', context)

def login_info(request):
	return render(request, 'ckmg/login.html')

def header_info(request):
	return render(request, 'ckmg/header.html')

def footer_info(request):
	return render(request, 'ckmg/footer.html')

def aboutus_info(request):
	return render(request, 'ckmg/aboutus.html')

def theorynotes_info(request):
	subject_list = subject.objects.all().filter(subject_catagary="CoS")
	context = {'subject_list':subject_list }
	return render(request, 'ckmg/theorynotes.html', context)

def theorynotes_subject(request, pm):
	#current_branch = branch.objects.get(branch_title=b_name)
	if pm == "CoS":
		subject_list = subject.objects.all().filter(subject_catagary="CoS")
	elif pm == "FA":
		subject_list = subject.objects.all().filter(subject_catagary="FA")
	elif pm == "MR":
		subject_list = subject.objects.all().filter(subject_catagary="MR")
	elif pm == "HR":
		subject_list = subject.objects.all().filter(subject_catagary="HR")
	else:
		subject_list = subject.objects.all().filter(subject_catagary="CoS")
	context = {'subject_list':subject_list }
	return render(request, 'ckmg/theorynotes.html', context)


def modelpapers_info(request):
	subject_list = subject.objects.all().filter(subject_catagary="CoS")
	context = {'subject_list':subject_list }
	return render(request, 'ckmg/modelpapers.html', context)

def modelpapers_subject(request, pm):
	#current_branch = branch.objects.get(branch_title=b_name)
	if pm == "CoS":
		subject_list = subject.objects.all().filter(subject_catagary="CoS")
	elif pm == "FA":
		subject_list = subject.objects.all().filter(subject_catagary="FA")
	elif pm == "MR":
		subject_list = subject.objects.all().filter(subject_catagary="MR")
	elif pm == "HR":
		subject_list = subject.objects.all().filter(subject_catagary="HR")
	else:
		subject_list = subject.objects.all().filter(subject_catagary="CoS")
	context = {'subject_list':subject_list }
	return render(request, 'ckmg/modelpapers.html', context)



def ppt_info(request):
	subject_list = subject.objects.all().filter(subject_catagary="CoS")
	context = {'subject_list':subject_list }
	return render(request, 'ckmg/ppt.html', context)

def ppt_subject(request, pm):
	#current_branch = branch.objects.get(branch_title=b_name)
	if pm == "CoS":
		subject_list = subject.objects.all().filter(subject_catagary="CoS")
	elif pm == "FA":
		subject_list = subject.objects.all().filter(subject_catagary="FA")
	elif pm == "MR":
		subject_list = subject.objects.all().filter(subject_catagary="MR")
	elif pm == "HR":
		subject_list = subject.objects.all().filter(subject_catagary="HR")
	else:
		subject_list = subject.objects.all().filter(subject_catagary="CoS")
	context = {'subject_list':subject_list }
	return render(request, 'ckmg/ppt.html', context)

def project_info(request):
	project_list = project.objects.all()
	context = {'project_list':project_list}
	return render(request, 'ckmg/projects.html', context)

def businessplan_info(request):
	businessplan_list = buisness_plan.objects.all()
	context = {'businessplan_list':businessplan_list}
	return render(request, 'ckmg/businessplan.html', context)

def service_info(request):
	return render(request, 'ckmg/services.html')

def training_info(request):
	return render(request, 'ckmg/training.html')

def guidance_info(request):
	return render(request, 'ckmg/guidance.html')

def contact_info(request):
	if request.method == 'GET':
		return render(request, 'ckmg/contactus.html')
	else:
		''' -----fetching the data from the user and saving it in database---- '''
		data = contactus(fname= request.POST['fname'], subject= request.POST['subname'], email = request.POST['email'], phone_no = request.POST['phone_no'], message = request.POST['message'])
		data.save()
		return HttpResponseRedirect('#')
