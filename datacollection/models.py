from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    reg_date = models.DateTimeField('registration date', auto_now=True)

    def __str__(self):
        return self.name