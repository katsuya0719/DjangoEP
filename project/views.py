from django.shortcuts import render
from project.models import html
from project.forms import htmlForm

# Create your views here.
def model_form_upload(request):
	if request.method=='POST':
		form=htmlForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=htmlForm()
	return render(request,'project/model_form_upload.html',{'form':form})
