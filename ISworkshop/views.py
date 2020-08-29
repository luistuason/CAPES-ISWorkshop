from django.shortcuts import render

# Create your views here.
def index(request):
  context = { }

  return render(request, 'ISworkshop/index.html', context=context)

def profile(request):
  context = { }

  return render(request, 'ISworkshop/profile.html', context=context)

def form(request):
  context = { }

  return render(request, 'ISworkshop/form.html', context=context)