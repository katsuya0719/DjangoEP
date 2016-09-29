from django.shortcuts import render
from project.models import html
from project.forms import DocumentForm
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from libs.EPprocessing.main import ProcessHtml
#from EnergyPlus import settings 
from django.core.files import File
import os
import pandas

# Create your views here.
class ListView(ListView):
	#model=html
	queryset=html.objects.all()
	#print(queryset)
	template_name='project_list.html'

class DetailView(DetailView):
	model=html
	template_name='project_detail.html'

def model_form_upload(request):
	#print(request.FILES)
	if request.method=='POST':
		form=DocumentForm(request.POST,request.FILES)
		if form.is_valid():
			newDoc=form.save()
			#newDoc=html(html=request.FILES['html'])
			newDoc.save()
			
			queryset=html.objects.all().last()
			dest=os.path.dirname(queryset.html.path)

			process_html(queryset.html.path,dest)
			
			#return HttpResponseRedirect('heat')
			return HttpResponse("success")
			#return redirect('home')
	else:
		form=DocumentForm()

	#print(form)
	return render(request,'model_form_upload.html',{'form':form})
	documents=html.objects.all()

def process_html(html,dest):
	case=ProcessHtml(file=html)
	db=case.extract_html()
	print (db["Area"])
	case.export_all(dest)
	#print(case.db)
	#print(documents)
	#return HttpResponse("success")
	#return render(request,'list.html',{'documents':documents, 'form':form})

