from django.shortcuts import render
from project.models import html
from project.forms import DocumentForm
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.list import ListView
from libs.EPprocessing.main import ProcessHtml
from EnergyPlus import settings 
from django.core.files import File
import os


# Create your views here.
class ListView(ListView):
	#model=html
	queryset=html.objects.all()
	#print(queryset)
	template_name='project_list.html'


def model_form_upload(request):
	#print(request.FILES)
	if request.method=='POST':
		form=DocumentForm(request.POST,request.FILES)
		if form.is_valid():
			newDoc=form.save()
			#newDoc=html(html=request.FILES['html'])
			newDoc.save()
			
			#process html
			"""
			html=request.FILES['html']
			f=open(html,'r')
			new=File(f)
			print(new)
			if html.multiple_chunks()==False:
				file=html.read()
			#print(file)
			#print(html.name)
			#print(html.chunks())
			"""
			queryset=html.objects.all().last()
			print(queryset.html.path)
			print(settings.MEDIA_ROOT)
			strHtml=os.path.join(settings.MEDIA_ROOT,queryset.html.path)
			process_html(strHtml)
			
			#return HttpResponseRedirect('heat')
			return HttpResponse("success")
			#return redirect('home')
	else:
		form=DocumentForm()

	#print(form)
	return render(request,'model_form_upload.html',{'form':form})
	documents=html.objects.all()

def process_html(html):
	case=ProcessHtml(file=html)
	case.extract_html()
	print(case.db)
	#print(documents)
	#return HttpResponse("success")
	#return render(request,'list.html',{'documents':documents, 'form':form})
