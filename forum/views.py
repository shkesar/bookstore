from django.shortcuts import render, redirect

from . import models
from . import forms

def index(request):
	if request.method == 'POST':
		document = models.Document(docfile=request.FILES['docfile'])
		document.save()
		redirect('forum:index')

	documents = models.Document.objects.all()
	
	return render(request, 'index.html',
		{'documents': documents})