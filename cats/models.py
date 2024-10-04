from django.db import models
from django.core.validators import MinLengthValidator as mv
# Create your models here.

class Breed(models.Model):
    name=models.CharField(
        max_length=200,
        validators=[mv (2,"Breed must be greater than ! character")]
        )

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[mv(1,"Your cat loves You ! give it a nickname Dang it!!")]
        )
    weight = models.PositiveIntegerField()
    foods= models.CharField(max_length=300)
    breed=models.ForeignKey('Breed', on_delete = models.CASCADE, null=False)

    def __str__(self):
        return self.nickname




















