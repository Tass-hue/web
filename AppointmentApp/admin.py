from django.contrib import admin
from .models import Appointment


@admin.action(description="make them confirmed")
def confirmed_appointment(modeladmin, request, queryset):
    queryset.update(status='CONFIRMED')


@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    actions = [confirmed_appointment]
    list_display = ("reason", "status", "duration_minutes", "appointment_date")
    list_filter = ("status", "appointment_date")
    list_editable = ("status",)
    search_fields = ("reason", "status")
    ordering = ("-appointment_date",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ('description', {'fields': ('reason', 'prescription', 'status')}),
        ('Date + Duration', {'fields': ('appointment_date', 'duration_minutes')}),
        ('Patients/Doctors', {'fields': ('doctor', 'patient')}),
        ('Planification', {'fields': ('created_at', 'updated_at')}),
    )