from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class User(AbstractUser):
    # Add any additional fields you want for the user model
    pass
class doctor(User):
    # Add any additional fields you want for the user model
    licence_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6), MaxLengthValidator])
    phone_number = models.CharField(max_length=8, unique=True, validators=[number_validation])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialities = models.ManyToManyField(
        "AccountApp.Speciality",
        related_name="doctors",
    ) 
    number_validation= RegexValidator(
            regex=r'^\d{8}$',
            message='le numéro de téléphone doit contenir exactement 8 chiffres.',
        )
def validate_birth_date(v):
    if v > timezone.localize(datetime.now()).date():
        raise ValidationError("La date de naissance ne peut pas être dans le futur.")
class patient(User):
    # Add any additional fields you want for the user model
    national_id = models.CharField(max_length=8, unique=True, validators=[number_validation])
    phone_number = models.CharField(max_length=8, validators=[number_validation])
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Speciality(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

