from django.core import validators
from django.db import models


class Create(models.Model):

    pro_name = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    purchase_date = models.DateField()
    mobile_no = models.CharField(max_length=20, validators=[validators.RegexValidator('[7-9]{1}+[0-9]{9}')])
    issue = models.TextField()


