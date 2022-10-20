from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=100)
    techStack = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=400)
    link = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.link
 
    class Meta:
        verbose_name_plural = 'Projects'
