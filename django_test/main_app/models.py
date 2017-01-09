from django.db import models

# Create your models here.
class poi(models.Model):
    name = models.CharField(max_length=50)
    relative_skill = models.CharField(max_length=200)
    priority = models.IntegerField()
    category = models.CharField(max_length=50)
    progress = models.IntegerField()

    def __str__(self):
        return self.name
