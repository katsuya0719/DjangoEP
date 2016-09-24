from django import forms
from project.models import html

"""
class htmlForm(forms.ModelForm):
	class Meta:
		model=html
		#fields=('html','uploaded_at',)
		fields=('html',)
"""
class DocumentForm(forms.Form):
	docfile=forms.FileField(label='Select a file')

	