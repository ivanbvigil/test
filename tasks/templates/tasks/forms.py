from django import forms
from .models import Task

class ProductForm(forms.Model):
	class Meta:
		model = Task
		fields = ['title', 'body', 'image']