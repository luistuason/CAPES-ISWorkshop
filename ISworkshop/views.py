from django.shortcuts import render
from .models import ProfilePage

def index(request):
  context = { }
  return render(request, 'ISworkshop/index.html', context=context)

def profile(request):
  posts = ProfilePage.objects.all()
  return render(request, 'ISworkshop/profile.html', {'posts': posts})

def form(request):
  context = { }
  return render(request, 'ISworkshop/form.html', context=context)