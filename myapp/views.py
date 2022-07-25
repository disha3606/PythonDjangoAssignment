from django.shortcuts import render
from .forms import CarForm
from .models import Car
from django.views import View

class HomeView(View):
 def get(self, request):
  form = CarForm()
  candidates = Car.objects.all()
  return render(request, 'myapp/home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = CarForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'myapp/home.html', {'form':form})

class CandidateView(View):
 def get(self, request, pk):
  candidate = Car.objects.get(pk=pk)
  return render(request, 'myapp/candidate.html', {'candidate':candidate})