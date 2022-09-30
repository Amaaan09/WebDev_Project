from django.db import models

# Create your models here.

class User(models.Model):
    designation_choices = (
    ('student','STUDENT'),
    ('teacher', 'TEACHER')
    )
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    designation = models.CharField(max_length=7, choices=designation_choices, default='student')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Users'


class Student(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    hours_watched = models.FloatField(max_length=100)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Students'


