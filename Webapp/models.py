from django.db import models

# Create your models here.
class Religion(models.Model):
    religion_id=models.IntegerField()
    religion_name=models.CharField(max_length=10)
    religion_flag=models.ImageField(upload_to ='uploads/')