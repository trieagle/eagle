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
        return datetime.datetime.now() >= self.begin_time and \
                datetime.datetime.now() <= self.end_time

    def debug(func):
        def wrapper(self):
            return True
        return wrapper

    @debug
    def done(self):
        is_done = False
        try:
            last_done = Status.objects.filter(task=self).latest("time")
        except Status.DoesNotExist:
            return is_done


        if last_done:
            cur = datetime.datetime.now()
            is_done = {
                TAG_TASK: lambda: True,
                ONCE_TASK: lambda: True,
                DAY_TASK: lambda: last_done.time.day >= cur.day,
                WEEK_TASK: lambda: last_done.time.day >= cur.day - \
                            datetime.datetime.weekday(cur) + 1,
                MONTH_TASK: lambda: last_done.time.month >= cur.month,
                YEAR_TASK: lambda: last_done.time.year >= cur.year
                }.get(self.mode)()
            return is_done

    def __unicode__(self):
        return str(self.id) + self.title

    class Meta:
        ordering = ['title']


def in_today(a_task):
    return a_task.begin_time.year == datetime.datetime.now().year and \
            a_task.begin_time.month == datetime.datetime.now().month and \
            a_task.begin_time.day == datetime.datetime.now().day


class Status(models.Model):
    task = models.ForeignKey(Task)
    rate = models.IntegerField(default=5)
    time = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['-time']
