from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import User

def validate_not_future_year(value):
    if value > date.today().year:
        raise ValidationError('Kelajak yili kiritilmasin.')

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    published_year = models.PositiveIntegerField(validators=[validate_not_future_year])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)