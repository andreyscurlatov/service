from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recruit(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recruit-detail',args=[str(self.id)])

class Sith(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sith-detail',args=[str(self.id)])

class Question(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Answer(models.Model):
    uid=models.IntegerField(default=0)
    recruit=models.ForeignKey(Recruit, on_delete=models.CASCADE, null=True)
    question=models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer=models.BooleanField(default=False)

class HandShadow(models.Model):
    recruit=models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name='hands')
    sith=models.ForeignKey(Sith, on_delete=models.CASCADE, null=True)







