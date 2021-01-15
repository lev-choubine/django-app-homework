from django.shortcuts import render
from .models import Sound
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def sounds_show(request):
  sounds = Sound.objects.all()
  return render(request, 'sounds/show.html', { 'sounds' : sounds})

class SoundCreate(CreateView):
  model = Sound
  fields = '__all__'
  success_url = '/sounds'

  def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.user = self.request.user
      self.object.save()
      return HttpResponseRedirect('/sounds')

class SoundUpdate(UpdateView):
  model = Sound
  fields = ['name', 'link', 'description']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/sounds')

class SoundDelete(DeleteView):
  model = Sound
  success_url = '/sounds'