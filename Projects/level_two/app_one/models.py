from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 256, unique=False)
    last_name = models.CharField(max_length = 256, unique=False)
    email = models.EmailField(max_length = 256, unique = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
