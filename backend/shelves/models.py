from django.db import models

class Book(models.Model):
    id = models.CharField(max_length=256, primary_key=True, unique=True)
    title = models.CharField(max_length=256)
    cover_url = models.CharField(max_length=256,blank=True)

    def __str__(self):
        return self.title
