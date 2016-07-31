from django.shortcuts import render, redirect

from . import models
from . import forms

def index(request):
    threads = models.Thread.objects.all()
    thread_form = forms.Thread()
    post_form = forms.Post()

    return render(request, 'chan/index.html',{
        'threads':threads,
        'thread_form':thread_form,
        'post_form':post_form,
    })

def create_post(request, thread_id):
    form = forms.Post(request.POST, request.FILES)
    if form.is_valid():
        post = Post(
            text=request.POST['text'],
            document=request.FILES['document'],
            thread=models.Thread.get(pk=thread_id),
        )
        post.save()
    return redirect('chan:index')

def create_thread(request):
    form = forms.Thread(request.POST, request.FILES)
    if form.is_valid():
        thread = Thread(
            text=request.POST['text'],
            document=request.FILES['document']
        )
        thread.save()
    return redirect('chan:index')
