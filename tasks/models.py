from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    priority = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'tasks' 