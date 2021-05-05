from django.db import models

# Create your models here.
class check(models.Model):
    pincode = models.IntegerField(default='000000')
    date_of_check = models.CharField(default='00-00-0000',max_length=10)

    def __str__(self):
        return self.date_of_check
