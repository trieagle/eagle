from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Routine(models.Model): 
    title = models.CharField(max_length=100) 
    details = models.CharField(max_length=1000) 
    owner = models.ForeignKey(User) 
    start_date = models.DateField()
    end_date = models.DateField()
    mode = models.IntegerField()#0 for one time, 1 daily, 2 weekly, 3 monthly, 4 yearly
    def __unicode__(self):
	return self.title
    class Meta:
        ordering = ['title']
    class Admin:
        pass

class Status(models.Model):
    routine = models.ForeignKey(Routine)
    user = models.ForeignKey(User)
    rate = models.IntegerField()#1-10
    date = models.DateField()

class Case(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    setup_date = models.DateField()
    

class Casething(models.Model):
    title = models.CharField(max_length=100) 
    details = models.CharField(max_length=1000) 
    owner = models.ForeignKey(User)
    case = models.ForeignKey(Case)
    setup_date = models.DateField()
    def __unicode__(self):
        return self.title
