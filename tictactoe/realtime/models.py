from django.db import models

# Create your models here.


class SecondClient(models.Model):
    group_name = models.CharField(max_length=20)
    first_client = models.CharField(max_length=30, null=True)
    second_client = models.CharField(max_length=30, null=True)
