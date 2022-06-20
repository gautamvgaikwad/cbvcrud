from django.db import models

# Create your models here.
class Empdata(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    contact_no=models.IntegerField()
    designation=models.CharField(max_length=50)


