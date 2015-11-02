from django.shortcuts import render, get_object_or_404, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from ckmg.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from forms import MyRegistrationForm

# Create your views here.
def index(request):
	slider_img = slider_image.objects.all()
	mrnews_list = news.objects.all().filter(news_type="MN")
	hrnews_list = news.objects.all().filter(news_type="HRN")
	fanews_list = news.objects.all().filter(news_type="FN")
	conews_list = news.objects.all().filter(news_type="CO")
	advertisements = advertise.objects.all()
	context = {'slider_img':slider_img, 'mrnews_list':mrnews_list, 'hrnews_list':hrnews_list, 'fanews_list':fanews_list, 'conews_list':conews_list, 'advertisements':advertisements, 'full_name': request.user.username}
	return render(request, 'ckmg/index.html', context)

def header_info(request):
	return render(request, 'ckmg/header.html', {'full_name': request.user.username})

def footer_info(request):
	return render(request, 'ckmg/footer.html')

def aboutus_info(request):
	return render(request, 'ckmg/aboutus.html', {'full_name': request.user.username})

#Mind Program views
def dmit_info(request):
	return render(request, 'ckmg/dmitanalysis.html', {'full_name': request.user.username})

def urja_info(request):
	return render(request, 'ckmg/urja.html', {'full_name': request.user.username})

def success_club_info(request):
	return render(request, 'ckmg/success_club.html', {'full_name': request.user.username})
 

#Librery views
@login_required
def theorynotes_info(request):
	subject_list = subject.objects.all().filter(subject_catagary="CoS")
	context = {'subject_list':subject_list, 'full_name': request.user.username}
	return render(request, 'ckmg/theorynotes.html', context)

@login_required
def theorynotes_subject(request, pm):
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
	context = {'subject_list':subject_list, 'full_name': request.user.username }
	return render(request, 'ckmg/theorynotes.html', context)

@login_required
def modelpapers_info(request):
	subject_list = subject.objects.all().filter(subject_catagary="CoS")
	context = {'subject_list':subject_list, 'full_name': request.user.username }
	return render(request, 'ckmg/modelpapers.html', context)

@login_required
def modelpapers_subject(request, pm):
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
	context = {'subject_list':subject_list, 'full_name': request.user.username}
	return render(request, 'ckmg/modelpapers.html', context)


@login_required
def ppt_info(request):
	subject_list = subject.objects.all().filter(subject_catagary="CoS")
	context = {'subject_list':subject_list, 'full_name': request.user.username}
	return render(request, 'ckmg/ppt.html', context)

@login_required
def ppt_subject(request, pm):
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
	context = {'subject_list':subject_list, 'full_name': request.user.username}
	return render(request, 'ckmg/ppt.html', context)

def project_info(request):
	project_list = project.objects.all()
	context = {'project_list':project_list, 'full_name': request.user.username}
	return render(request, 'ckmg/projects.html', context)

def businessplan_info(request):
	businessplan_list = buisness_plan.objects.all()
	context = {'businessplan_list':businessplan_list, 'full_name': request.user.username}
	return render(request, 'ckmg/businessplan.html', context)


#services views
def service_info(request):
	return render(request, 'ckmg/services.html', {'full_name': request.user.username})

def training_info(request):
	return render(request, 'ckmg/training.html', {'full_name': request.user.username})

def guidance_info(request):
	return render(request, 'ckmg/guidance.html', {'full_name': request.user.username})


def contact_info(request):
	if request.method == 'GET':
		return render(request, 'ckmg/contactus.html', {'full_name': request.user.username})
	else:
		''' -----fetching the data from the user and saving it in database---- '''
		data = contactus(fname= request.POST['fname'], subject= request.POST['subname'], email = request.POST['email'], phone_no = request.POST['phone_no'], message = request.POST['message'])
		data.save()
		return HttpResponseRedirect('#')


# user login, Registeration and authentication views
def login(request):
	context = {}
	context.update(csrf(request))
	return render_to_response('ckmg/login.html',context)


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user:
		auth.login(request, user)
		return HttpResponseRedirect("/accounts/loggedin")
	else:
		return HttpResponseRedirect("/accounts/invalid")


def loggedin(request):
	slider_img = slider_image.objects.all()
	mrnews_list = news.objects.all().filter(news_type="MN")
	hrnews_list = news.objects.all().filter(news_type="HRN")
	fanews_list = news.objects.all().filter(news_type="FN")
	conews_list = news.objects.all().filter(news_type="CO")
	advertisements = advertise.objects.all()
	context = {'slider_img':slider_img, 'mrnews_list':mrnews_list, 'hrnews_list':hrnews_list, 'fanews_list':fanews_list, 'conews_list':conews_list, 'advertisements':advertisements, 'full_name': request.user.username}
	return render_to_response('ckmg/index.html', context)


def invalid_login(request):
	return render_to_response('ckmg/invalid_login.html')


def logout(request):
	auth.logout(request)
	slider_img = slider_image.objects.all()
	mrnews_list = news.objects.all().filter(news_type="MN")
	hrnews_list = news.objects.all().filter(news_type="HRN")
	fanews_list = news.objects.all().filter(news_type="FN")
	conews_list = news.objects.all().filter(news_type="CO")
	advertisements = advertise.objects.all()
	context = {'slider_img':slider_img, 'mrnews_list':mrnews_list, 'hrnews_list':hrnews_list, 'fanews_list':fanews_list, 'conews_list':conews_list, 'advertisements':advertisements, 'full_name': request.user.username}
	return render_to_response('ckmg/index.html', context)


def register_user(request):
    if request.method == 'POST':

        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login")
    else:
        form = MyRegistrationForm()
    return render(request, "ckmg/signup.html", {'form': form,})


def register_success(request):
    return render_to_response('ckmg/login.html')


	
