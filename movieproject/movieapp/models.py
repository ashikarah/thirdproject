from django.db import models

class movie(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
