from django import forms
class PatientForm(forms.Form):
    nom=forms.CharField()
    prenom=forms.CharField()
    email=forms.EmailField()
    date_de_naissance=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    hidden_input=forms.CharField(widget=forms.HiddenInput,initial="Hidden value")
