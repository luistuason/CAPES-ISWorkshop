from django.shortcuts import render
from .models import ProfilePage

def index(request):
  posts = ProfilePage.objects.all()
  return render(request, 'ISworkshop/profile.html', {'posts': posts})

def profile(request):
  context = { }

  return render(request, 'ISworkshop/profile.html', context=context)

def form(request):
  context = { }

  return render(request, 'ISworkshop/form.html', context=context)