from django.contrib import admin
from .models import User, doctor, patient, Speciality
from AppointmentApp.models import Appointment


class AppointmentStacked(admin.StackedInline):
    model = Appointment
    extra = 1


@admin.register(doctor)
class DoctorPersoClass(admin.ModelAdmin):
    inlines = [AppointmentStacked]


admin.site.register(User)
admin.site.register(patient)
admin.site.register(Speciality)