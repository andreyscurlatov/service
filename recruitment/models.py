from django.db import models
from django.urls import reverse
from django.db.models import signals
from recruitment.tasks import sendMail

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recruit(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    email = models.EmailField(max_length=100, verbose_name='Электронный адрес почты')

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
    text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    recruit=models.ForeignKey(Recruit, on_delete=models.CASCADE, null=True)
    question=models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer=models.BooleanField(default=False)

class HandShadow(models.Model):
    recruit=models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name='hands')
    sith=models.ForeignKey(Sith, on_delete=models.CASCADE, null=True)
    isWelcomeMailSent=models.BooleanField(default=False)

    def __str__(self):
        return self.recruit.name

def handshadow_post_save(sender, instance, signal, *args, **kwargs):
    sendMail.delay(instance.id)

signals.post_save.connect(handshadow_post_save, sender=HandShadow)


