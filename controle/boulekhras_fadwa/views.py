from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Patient, Medecin, Rendez_vous
from .forms import PatientForm
from .rechercheForm import SearchForm


def index(request):
    patients = Patient.objects.all()
    p=Paginator(Patient.objects.all(),5)
    page=request.GET.get('page')
    patient_list=p.get_page(page)
    return render(request, 'patients.html', {'patients': patients,'patient_list':patient_list})

def medecins(request):
    medecins = Medecin.objects.all()
    p = Paginator(Medecin.objects.all(), 5)
    page = request.GET.get('page')
    medecins_list = p.get_page(page)
    return render(request, 'medecin.html', {'medecins': medecins,'medecins_list':medecins_list})

def details(request, id):
    patient = Patient.objects.get(id=id)
    context = {'patient': patient}
    return render(request, 'details.html', context)
def rendez_vous(request, id):

    rdv = Rendez_vous.objects.get(patient__id=id)
    context = {'rdv': rdv}
    return render(request, 'rendez_vous.html',context)

def delete(request, id):
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return redirect('/hopital')
    patient.delete()
    return redirect('/hopital')
def update(request, id):
    patient = Patient.objects.get(id=id)
    context = {'patient': patient}
    return render(request, 'update.html', context)

def edit(request,id):
    patient = Patient.objects.get(id=id)
    patient.nom=request.POST.get("nom", "").capitalize()
    patient.prenom=request.POST.get("prenom", "").capitalize()
    patient.email=request.POST.get("email", "").capitalize()
    patient.ddn = request.POST.get("dateNaissance")
    patient.save()
    return redirect("/hopital")

def addPatient(request):
    return render(request,"addPatient.html")


def create(request):
    nom = request.POST.get("nom", "").capitalize()
    prenom = request.POST.get("prenom", "").capitalize()
    email = request.POST.get("email", "")
    dateNaissance = request.POST.get("dateNaissance")
    patient = Patient.objects.create(nom=nom,prenom=prenom,ddn=dateNaissance,email=email)
    patient.save()
    return redirect("/hopital")
def search(request):
    if request.method=="POST":
        q=request.POST.get("q", "")
        patient=Patient.objects.filter(nom__contains=q)
        return render(request,'search.html',{'q':q,'patient': patient})
def medSearch(request):
    if request.method=="POST":
        q=request.POST.get("q", "")
        med=Medecin.objects.filter(nom__contains=q)
        return render(request,'searchMed.html',{'q':q,'med': med})

def formView(request):
    form=PatientForm()
    return render(request,"addPatient.html",{"form":form})
def searchForm(request):
    form=SearchForm()
    return render(request,"patients.html",{"form":form})