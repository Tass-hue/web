from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


number_validation = RegexValidator(
    regex=r'^\d{8}$',
    message='le numéro de téléphone doit contenir exactement 8 chiffres.',
)


def validate_birth_date(v):
    if v > timezone.now().date():
        raise ValidationError("La date de naissance ne peut pas être dans le futur.")


class User(AbstractUser):
    pass


class doctor(User):
    licence_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)])
    phone_number = models.CharField(max_length=8, unique=True, validators=[number_validation])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialities = models.ManyToManyField(
        "AccountApp.Speciality",
        related_name="doctors",
    )
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

class patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[number_validation])
    phone_number = models.CharField(max_length=8, validators=[number_validation])
    birth_date = models.DateField(validators=[validate_birth_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

class Speciality(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"
    def __str__(self):
        return self.name