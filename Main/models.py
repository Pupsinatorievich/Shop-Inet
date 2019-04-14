from django.db import models
from django import forms

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return "Пользователь {} {}".format(self.name, self.email)
    
    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscriber"
   
    
class SubscribersForms(forms.ModelForm):
    
    class Meta:
        model = Subscriber
        exclude = [""]
        
