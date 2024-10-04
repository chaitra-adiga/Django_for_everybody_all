from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Enter a make (e.g. Renault)',
        validators=[MinLengthValidator(2,"Make must be greater than 1 character ")]
    )

    def __str__(self):
        return self.name


class Auto(models.Model):
    nickname=models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2,"Nickname must minimum 2 characters long")]

        )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.nickname
