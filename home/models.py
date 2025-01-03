import warnings
warnings.filterwarnings('ignore')
from django.db import models
from django.utils.timezone import now


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=2500)
    date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'contacts'
        managed = True