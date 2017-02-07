from django.db import models
from django.core.validators import RegexValidator
import warnings
warnings.filterwarnings("ignore", "Field 'subbranch_title' doesn't have a default value")


class contactus(models.Model):
	fname = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	phone_no = models.IntegerField(blank=True)
	message = models.TextField(max_length=5000)

	def __unicode__(self):              
        	return str(self.fname) 


class news(models.Model):
	news_title = models.CharField(max_length=100)
	link = models.CharField(max_length=200,default="https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxkcmNoaXRyYWRoYXdhbGV8Z3g6NDQzYzkwN2Y3YzY2ZWRjYw")
	date = models.DateField(auto_now=False, auto_now_add=False)
	news_type_choices = (
		('MN', 'Marketing News'),
    	('HRN', 'HR News'),
    	('FN', 'Finance News'),
    	('CO', 'Current Opening'),
		)
	news_type = models.CharField(max_length=3, choices=news_type_choices, default='MN')

	def __unicode__(self):
		return self.news_title
		

class subject(models.Model):
	subject_name = models.CharField(max_length=100)
	subject_catagary_chices = (
		('CoS', 'Core Subject'),
    	('MR', 'Marketing'),
    	('FA', 'Finance'),
    	('HR', 'Human Resource'),
		)
	subject_catagary = models.CharField(max_length=3, choices=subject_catagary_chices, default='MR')

	def __unicode__(self):
		return self.subject_name
	

class result(models.Model):
	batch = models.CharField(max_length=20)
	year = models.IntegerField(default=2011)
	student_name = models.CharField(max_length=50)
	college_name = models.CharField(max_length=100)
	course = models.CharField(max_length=100)
	date = models.DateField(auto_now=False, auto_now_add=False)
	def __unicode__(self):
		return self.student_name

				
class advertise(models.Model):
	advertiser_name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="Images/Advertisement")
	html_link = models.CharField(max_length=200,default="https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxkcmNoaXRyYWRoYXdhbGV8Z3g6NDQzYzkwN2Y3YzY2ZWRjYw")
	status_choice = (
		('A', 'activate'),
		('D', 'deactivate'),
		)
	status = models.CharField(max_length=1, choices=status_choice, default='D')
	date = models.DateField(auto_now=False, auto_now_add=False)  
	def __unicode__(self):
		return self.advertiser_name
		

class alumni(models.Model):
	batch = models.CharField(max_length=20)
	year = models.IntegerField(default=2011)
	student_name = models.CharField(max_length=50)
	college_name = models.CharField(max_length=100)
	course = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	date = models.DateField(auto_now=False, auto_now_add=False)
	def __unicode__(self):
		return self.student_name


class buisness_plan(models.Model):
	buisness_title = models.CharField(max_length=100)
	buisnessplan_desc = models.TextField(max_length=5000, default="Buisness Plan Describtion")
	pdf_file = models.FileField(upload_to="Docs/buisness_plan/pdf")
	ppt_file = models.FileField(upload_to="Docs/buisness_plan/ppt")
	date = models.DateField(auto_now=False, auto_now_add=False)
	def __unicode__(self):
		return self.buisness_title


class project(models.Model):
	project_title = models.CharField(max_length=100)
	project_desc = models.TextField(max_length=5000, default="Project Describtion")
	doc_file = models.FileField(upload_to="Docs/project/docfile")
	pdf_file = models.FileField(upload_to="Docs/project/pdf")
	date = models.DateField(auto_now=False, auto_now_add=False)
	def __unicode__(self):
		return self.project_title


class theorynotes(models.Model):
	notes_title = models.CharField(max_length=100)
	pdf_file = models.FileField(upload_to="Docs/Theory_Notes/pdf")
	ppt_file = models.FileField(upload_to="Docs/Theory_Notes/ppt")
	date = models.DateField(auto_now=False, auto_now_add=False)
	subject = models.ForeignKey(subject)
	def __unicode__(self):
		return self.notes_title


class ppt(models.Model):
	ppt_title = models.CharField(max_length=100)
	ppt_file = models.FileField(upload_to="Docs/PPT/ppt")
	date = models.DateField(auto_now=False, auto_now_add=False)
	subject = models.ForeignKey(subject)
	def __unicode__(self):
		return self.ppt_title


class modelpaper(models.Model):
	modelpaper_title = models.CharField(max_length=100)
	pdf_file = models.FileField(upload_to="Docs/Model_Paper/pdf")
	date = models.DateField(auto_now=False, auto_now_add=False)
	subject = models.ForeignKey(subject)
	def __unicode__(self):
		return self.modelpaper_title


class slider_image(models.Model):
	slider_image = models.ImageField(upload_to="Images/Slider/")
	image_quote = models.TextField(max_length=500,default="quote for image")

	def __unicode__(self):              
        	return self.image_quote	



		
		
		