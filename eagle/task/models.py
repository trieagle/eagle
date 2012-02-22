from django.db import models
from account import models as account_models
import datetime

class Tag(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField(default=datetime.datetime.now);
    def __unicode__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=30)
    detail = models.TextField(blank=True)
    priority = models.IntegerField(default=1)
    alive = models.IntegerField(default=1)
    
    #0 for tag thing, 1 once, 2 daily, 3 weekly, 4 monthly, 5 yearly
    mode = models.IntegerField()
    owner = models.ForeignKey(account_models.Account, 
                              related_name='task_owner');
    liker = models.ManyToManyField(account_models.Account,
                                   related_name='task_liker',
                                   blank=True)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    begin_time = models.DateTimeField(default=datetime.datetime.now)
    end_time = models.DateTimeField(default=datetime.datetime.now)
    tag = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['title']
    class Admin:
        pass





# Create your models here.
