from django.db import models

def dir_path(instance,filename):
	return 'html/{0}/{1}'.format(instance.project,filename)

# Create your models here.
class html(models.Model):
	project=models.CharField(max_length=50,blank=True)
	html=models.FileField(upload_to=dir_path)
	uploaded_at=models.DateTimeField(auto_now_add=True)

class basic(models.Model):
	html=models.OneToOneField(html,primary_key=True)
	total_area=models.IntegerField()
	condition_area=models.IntegerField()
	uncondition_area=models.IntegerField()

class electricity(models.Model):
	html=models.OneToOneField(html,primary_key=True)
	file=models.FileField(upload_to='electricity')

