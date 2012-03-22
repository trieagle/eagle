from eagle.task.models import *
from eagle.account.models import *

u1 = Account.objects.get(pk=2)
t1 = Tag.objects.create(name='atag1')
t2 = Tag.objects.create(name='atag2')

t1.save()
t2.save()

task1 = Task.objects.create(title='test 1', detail='this is the detail part of test 1', priority=2, mode = 1, owner=u1)

task2 = Task.objects.create(title='test 2 ', detail='this is the detail part of test 2', priority=2, mode = 2, owner=u1)

task3 = Task.objects.create(title='test 3 ', detail='this is the detail part of test  3', priority=2, mode = 3, owner=u1)

task1.tag.add(t1)
task2.tag.add(t2)
task3.tag.add(t1)

task1.save()
task2.save()
task3.save()
