from django.db import models

# Create your models here.

class Lawyer(models.Model):
    name = models.CharField(max_length=100, null=True)
    picture = models.ImageField(upload_to='profile-picture/', null=True, blank=True)
    phoneno = models.CharField(max_length=13, null=True)
    education = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50, null=True)
    expertise = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.name