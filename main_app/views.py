from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from django.http import HttpResponse

# Create your views here.


def home(request): 
  return render(request, 'home.html')

def about(request): 
  return render(request, 'about.html')

def dogs_index(request): 
  dogs = Dog.objects.all()
  # print(dogs, 'THIS is a print inside of DOGS_INDEX')
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id): 
  dog = Dog.objects.get(id=dog_id)
  # print(dog, 'this is the id for the dog')
  return render(request, 'dogs/detail.html', { 'dog': dog })  

class DogCreate(CreateView): 
  model = Dog 
  fields = '__all__'

class DogUpdate(UpdateView): 
  model = Dog
  fields = ['name', 'breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'