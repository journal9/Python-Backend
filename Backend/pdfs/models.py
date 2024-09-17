from django.db import models

# Create your models here.
class Pdf(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='dummy')
    name = models.CharField(max_length=50)
