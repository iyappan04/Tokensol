from django.db import models

# Create your models here.
class Transaction(models.Model):
    amount = models.IntegerField(null=True, blank=True, max_length=24)
    types = models.CharField()

   