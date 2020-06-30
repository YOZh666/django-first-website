from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField('Name', max_length=55)
    task = models.TextField('Description')

    def __str__(self):
        return self.title