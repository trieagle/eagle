from django.contrib.auth import models as auth_models 
from django.db import models
"""
inherented from User
username(*),first_name,last_name,email,password,is_staff,is_active,is_superuser
last_login,date_joined

new  in Account
portrait gender description location school grade 
friends followers

"""
class Account(auth_models.User):
    portrait = models.ImageField('your portraint', upload_to="img/portrait")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, 
                              choices=GENDER_CHOICES, 
                              blank=True)
    description = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=20, blank=True) 
    school = models.CharField(max_length=20, blank=True) 
    grade = models.IntegerField(default=0)
    friends = models.ManyToManyField('self', blank=True)
    followers = models.ManyToManyField('self', blank=True)

    objects = auth_models.UserManager()


# Create your models here.
