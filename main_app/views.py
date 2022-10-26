from django.shortcuts import render
from .models import Dog
from django.http import HttpResponse

# Create your views here.
# Add the Cat class & list and view function below the imports
# class Dog:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# dogs = [
#   Dog('Lolo', 'huskey', 'foul little demon', 3),
#   Dog('Sachi', ' shepred', 'diluted tortoise shell', 0),
#   Dog('Raven', 'putbull', '3 legged dog', 4)
# ]


def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def dogs_index(request): 
    dogs = Dog.objects.all()
    print(dogs, 'THIS is a print inside of DOGS_INDEX')
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id): 
    dog = Dog.objects.get(id=dog_id)
    print(dog, 'this is the id for the dog')
    return render(request, 'dogs/detail.html', { 'dog': dog })  