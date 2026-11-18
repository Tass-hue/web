from django.db import models
from AccountApp.models import doctor, patient
# Create your models here.
class Appointment(models.Model):
    reason = models.CharField() 
    prescription = models.CharField(
        blank=True,
        upload_to='prescriptions/',
    )
    class Statut(models.TextChoices):
        PENDING = 'PENDING', 'en attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'
        status = models.CharField(max_length=10, choices=Statut.choices, default=Statut.PENDING)
       durattion_minutes = models.PositiveIntegerField(default=30)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(patient, on_delete=models.CASCADE, related_name='appointments')
