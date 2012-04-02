from django.db import models
from account import models as account_models
import datetime

class Tag(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField(default=datetime.datetime.now);
    def __unicode__(self):
        return self.name

TAG_TASK, ONCE_TASK, DAY_TASK, WEEK_TASK, MONTH_TASK, YEAR_TASK = range(6)

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
    privacy = models.IntegerField(default=0)

    def active(self):
        return alive==1 and datetime.datetime.now() >= self.begin_time and \
            datetime.datetime.now() <= self.end_time

    def done(self):
        is_done = False
        last_done = Status.objects.filter(task=self).latest("time")
        if last_done:
            cur = datetime.datetime.now()
            if self.mode == TAG_TASK:
                is_done = True
            elif self.mode == ONCE_TASK:
                is_done = True
            elif self.mode == DAY_TASK:
                if last_done.time.day >= cur.day:
                    is_done = True
            elif self.mode == WEEK_TASK:
                if last_done.time.day >= cur.day-datetime.datetime.weekday(cur) + 1:
                    is_done = True
            elif self.mode == MONTH_TASK:
                if last_done.time.month >= cur.month:
                    is_done = True
            elif self.mode == YEAR_TASK:
                if last_done.time.year >= cur.year:
                    is_done = True	
            return is_done
    def in_today(a_task):
        return a_task.year == datetime.datetime.now().year and \
            a_task.month == datetime.datetime.now().month and \
            a_task.day == datetime.datetime.now().day


    def __unicode__(self):
        return str(self.id) + self.title

    class Meta:
        ordering = ['title']


class Status(models.Model):
    task = models.ForeignKey(Task)
    rate = models.IntegerField(default=5)
    time = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['-time']
