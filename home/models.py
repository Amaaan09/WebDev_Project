from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    designation_choices = (
    ('student','STUDENT'),
    ('teacher', 'TEACHER')
    )
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    # fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    designation = models.CharField(max_length=7, choices=designation_choices, default='student')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'Profile'


class Student(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    # fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    hours_watched = models.FloatField(max_length=100)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'Students'


