from django.urls import path
from . import views
urlpatterns = [
    path('hopital/', views.index),
    path('medecin', views.medecins),
    path('addPatient/', views.addPatient),
    path('hopital/create', views.create,name="create"),
    path('hopital/delete/<int:id>', views.delete),
    path('hopital/details/<int:id>', views.details),
    path('hopital/rendez_vous/<int:id>', views.rendez_vous),
    path('hopital/update/<int:id>', views.update),
    path('hopital/edit/<int:id>', views.edit),
    path('hopital/search', views.search),
    path('hopital/searchMed', views.medSearch),
    path('hopital/form', views.formView)

]