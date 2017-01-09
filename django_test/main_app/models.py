from django.db import models

class poi(models.Model):
    name = models.CharField(max_length=50)
    relative_skill = models.CharField(max_length=200)
    priority = models.IntegerField(max_length = 1)
    category = models.CharField(max_length=50)
    progress = models.IntegerField(max_length=3)
    img_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name
