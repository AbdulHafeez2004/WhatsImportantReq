from django.db import models
from datetime import datetime

# Create your models here.


class Summary(models.Model):
    full_text = models.CharField(max_length=10000000)
    summary = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now=True)
