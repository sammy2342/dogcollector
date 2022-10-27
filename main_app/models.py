
from email.policy import default
from random import choices
from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
    ('B', 'Breakfast'), 
    ('L', 'Lunch'), 
    ('D', 'Dinner'),
)

class Toy(models.Model): 
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self): 
        return self.name 

    def get_absolute_url(self):
        return reverse('toys_details', kwargs={'pk': self.id})


class Dog(models.Model): 
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self): 
        return self.name 
    
    def get_absolute_url(self): 
        # print(self.id, 'thos osasdfsadasdfsadf')
        return reverse('detail', kwargs={'dog_id': self.id})

class Feeding(models.Model): 
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1, 
            choices=MEALS,
            default=MEALS[0][0]
    )
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.get_meal_display()} on {self.date}"

    class Meta: 
        ordering = ['date']