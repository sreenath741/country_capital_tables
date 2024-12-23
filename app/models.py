from django.db import models

# Create your models here.
class Country(models.Model):
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=100)
class Capital(models.Model):
    cap_id=models.IntegerField(primary_key=True)
    cap_name=models.CharField(max_length=100)
    c_id=models.ForeignKey(Country,on_delete=models.CASCADE)    