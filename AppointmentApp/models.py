from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from AccountApp.models import doctor, patient

class Appointment(models.Model):
    class Statut(models.TextChoices):
        PENDING = 'PENDING', 'en attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'

    reason = models.CharField(max_length=255)
    prescription = models.FileField(blank=True, upload_to='prescriptions/')
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=Statut.choices, default=Statut.PENDING)
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(patient, on_delete=models.CASCADE, related_name='appointments')

    def clean(self):
        modified_date = self._state.adding or (
            Appointment.objects.filter(
                pk=self.pk,appointment_date=self.appointment_date
            ).exists()
        )
        if modified_date and self.appointment_date < timezone.now():
            raise ValidationError("La date du rendez-vous doit être supérieure à la date actuelle.")
    class Meta:
        ordering = ["-appointment_date"]
        constraints = [
            models.UniqueConstraint(
                fields=["doctor", "appointment_date"],
                name="unicite_patient-doctor-date",
                violation_error_message="ce doctor possede un rdv avec cette date",
            )
        ]
    def __str__(self):
        return f"le rdv est pour la raisona"