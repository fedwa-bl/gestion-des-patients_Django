from django.db import models


class Patient(models.Model):
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    ddn=models.DateField(auto_now=True)
    def __str__(self):
        return self.nom

class Medecin(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    specialite = models.CharField(max_length=35)
    def __str__(self):
        return self.nom
class Rendez_vous(models.Model):
    date=models.DateField(auto_now=True)
    annuleYN=models.BooleanField(default=False)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin=models.ForeignKey(Medecin, on_delete=models.CASCADE)


class Consultation(models.Model):
    description = models.CharField(max_length=30)
    traitement = models.CharField(max_length=30)
    type = models.CharField(max_length=35)
    rendez_vous=models.ForeignKey(Rendez_vous, on_delete=models.CASCADE)
