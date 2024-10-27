from django.db import models

class todo_model(models.Model):
    todo = models.TextField(null=True)
    status = models.CharField(max_length=500, null=True, default='To Do')

    def __str__(self):
        return self.todo
