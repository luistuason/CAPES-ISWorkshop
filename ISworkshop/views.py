from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ProfilePage
from .forms import ProfilePageForm

def index(request):
  context = { }
  return render(request, 'ISworkshop/index.html', context=context)

def profile(request):
  posts = ProfilePage.objects.all()
  return render(request, 'ISworkshop/profile.html', {'posts': posts})

def editProfile(request):
  profile = ProfilePage.objects.get(pk=1)

  if request.method == 'POST':
    form = ProfilePageForm(request.POST, instance=profile)
    if form.is_valid():
      form.save()

      return HttpResponseRedirect('/ISworkshop/profile')
  else:
      form = ProfilePageForm(instance=profile)

  context = {'form': form}
  return render(request, 'ISworkshop/form.html', context=context)