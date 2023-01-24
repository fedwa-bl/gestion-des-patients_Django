from django.contrib import admin

from .models import Patient, Medecin, Rendez_vous, Consultation


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass
@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    pass
@admin.register(Rendez_vous)
class PatientAdmin(admin.ModelAdmin):
    pass
@admin.register(Consultation)
class PatientAdmin(admin.ModelAdmin):
    pass