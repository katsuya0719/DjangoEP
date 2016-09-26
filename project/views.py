from django.shortcuts import render
from project.models import html
from project.forms import DocumentForm
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.list import ListView


# Create your views here.
class ListView(ListView):
	model=html

	
def model_form_upload(request):
	#print(request.FILES)
	if request.method=='POST':
		form=DocumentForm(request.POST,request.FILES)
		print(form)
		if form.is_valid():
			newDoc=form.save()
			#newDoc=html(html=request.FILES['html'])
			print(newDoc)
			newDoc.save()
			
			#return HttpResponseRedirect('heat')
			return HttpResponse("success")
			#return redirect('home')
	else:
		form=DocumentForm()

	#print(form)
	return render(request,'model_form_upload.html',{'form':form})
	documents=html.objects.all()

	#print(documents)
	#return HttpResponse("success")
	#return render(request,'list.html',{'documents':documents, 'form':form})
