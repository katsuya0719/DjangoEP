from django.shortcuts import render
from project.models import html,basic
from project.forms import DocumentForm
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from libs.EPprocessing.main import ProcessHtml
#from EnergyPlus import settings 
from django.core.files import File
import os
import pandas
import dj_database_url
from django.conf import settings

# Create your views here.
class ListView(ListView):
	#model=html
	queryset=html.objects.all()
	#print(queryset)
	template_name='project_list.html'

class DetailView(DetailView):
	model=html
	template_name='project_detail.html'

	def get_context_data(self,**kwargs):
		data=super().get_context_data(**kwargs)
		print(len(settings.MEDIA_ROOT))
		#print(os.path.dirname(data["object"].html.path))
		#data["abspath"]=str(os.path.join((os.path.dirname(data["object"].html.path)),"Energy.csv"))
		abspath=str(os.path.join((os.path.dirname(data["object"].html.path)),"Energy.csv"))
		#data["strpath"]=abspath.translate(None,settings.MEDIA_ROOT)
		strpath=abspath[len(settings.MEDIA_ROOT):].replace("\\","/")
		data["strpath"]="../../static"+strpath
		print(data["strpath"])
		return data

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

			area=process_html(queryset.html.path,dest)
			register_df(area)

			#return HttpResponseRedirect('heat')
			return HttpResponse("success")
			#return redirect('home')
	else:
		form=DocumentForm()

	#print(form)
	return render(request,'model_form_upload.html',{'form':form})
	documents=html.objects.all()
"""
def register_df(df):
	
	database_name=settings.DATABASES['default']['NAME']
	database_url='sqlite://{database_name}'.format(
		database_name=database_name,
		)
	engine=create_engine(database_url,echo=False)
	df.to_sql(basic,con=engine)
"""
def register_df(df):
	print(basic._meta.get_fields())
	entries=[]
	for e in df.iloc[1:,1:].T.to_dict().values():
		print(basic.field)
		entries.append(basic(**e))

def process_html(html,dest):
	case=ProcessHtml(file=html)
	db=case.extract_html()
	print (db["Unmet"])
	case.export_all(dest)
	return db["Area"]
	#print(case.db)
	#print(documents)
	#return HttpResponse("success")
	#return render(request,'list.html',{'documents':documents, 'form':form})

