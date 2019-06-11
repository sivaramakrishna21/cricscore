from django.db import models

# Create your models here.

class Todolist(models.Model):
    name = models.CharField(max_length=128)
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural="todolist"
    def __str__(self):
        return self.name
class Todoitem(models.Model):
    description=models.CharField(max_length=128)
    duedate=models.DateField()
    completed=models.BooleanField()

    class Meta:
        verbose_name_plural = "todoitem"

    def __str__(self):
        return self.name
