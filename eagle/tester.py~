from eagle.task.models import *
from eagle.account.models import *
from django.contrib.auth.models import User

## generate user: eagle
username = "eagle"
email = "ealge@example.com"
password = "eagle"
user_obj = User.objects.create_user(username,email,password)
user_obj.save()

eagle = Account(user=user_obj)
eagle.save()


## generate tag: tag1,tag2

t1 = Tag.objects.create(name='tag1')
t2 = Tag.objects.create(name='tag2')
t1.save()
t2.save()

## generate task:task1,task2,task3

task1 = Task.objects.create(title='test 1 ', detail='this is the detail part of test 1', priority=1, mode = 1, owner = eagle)
task2 = Task.objects.create(title='test 2 ', detail='this is the detail part of test 2', priority=2, mode = 2, owner = eagle)
task3 = Task.objects.create(title='test 3 ', detail='this is the detail part of test  3', priority=2, mode = 3, owner = eagle)

task1.tag.add(t1)
task2.tag.add(t2)
task3.tag.add(t1)
task3.tag.add(t2)

task1.save()
task2.save()
task3.save()
