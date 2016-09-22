from django.db import models

# Create your models here.
class html(models.Model):
	html=models.FileField(upload_to='C:/Users/obakatsu/Documents/Python_scripts/Django/EnergyPlus/data')
	#uploaded_at=models.DateTimeField(auto_now_add=True)

