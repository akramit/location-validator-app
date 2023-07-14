from django.db import models

# Create your models here.
class location(models.Model):
    city = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.address