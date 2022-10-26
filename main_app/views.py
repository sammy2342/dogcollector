from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from .models import Dog, Toy
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
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', { 'dog': dog, 'feeding_form': feeding_form })  

def add_feeding(request, dog_id): 
  form = FeedingForm(request.POST)
  # print(form, 'this is the form data')
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    # print(new_feeding.dog_id, 'thsisidsids')
    new_feeding.save()
    return redirect('detail', dog_id=dog_id)

class DogCreate(CreateView): 
  model = Dog 
  fields = '__all__'

class DogUpdate(UpdateView): 
  model = Dog
  fields = ['name', 'breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

# or you can just put it in the main_app and it will automatically know without putting the temlate_name 
# I'm doing because this makes me understand it better
class ToyList(ListView): 
  model = Toy
  template_name = 'toys/toy_list.html'

class ToyDetail(DetailView): 
  model = Toy
  template_name = 'toys/toy_detail.html'


