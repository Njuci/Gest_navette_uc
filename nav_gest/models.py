from django.db import models
import datetime

# Create your models here.
class Moyen_Transport(models.Model):
    MT_TYPE_CHOICES = (
           ('bus', 'Bus'),
           ('coast', 'Coaster'),
           ('voi','Voiture Luxe')                      
       )
    
    nom_mt=models.CharField(max_length=70,unique=True,blank=True)
    capacite=models.IntegerField()
    type_voiture=models.CharField(max_length=5,choices=MT_TYPE_CHOICES)
    
class Assigner_Voiture(models.Model):
    id_user=models.ForeignKey('user_gest.Utilisateur',on_delete=models.CASCADE)
    id_voiture=models.ForeignKey(Moyen_Transport,on_delete=models.CASCADE)
    date_ass=models.DateField(auto_now_add=True)
    class Meta:
        unique_together=('id_user','id_voiture_id','date_ass')
    def __str__(self) -> str:
        return self.id_user.first_name + ' '+ self.id_user.last_name + ' ' + self.id_voiture.nom_mt + ' ' + str(self.date_ass)
    
class Course(models.Model):
    id_assignation=models.ForeignKey(Assigner_Voiture,on_delete=models.CASCADE)
    nombre_passager=models.IntegerField(default=0)
    carburant=models.FloatField(default=0.0)
    date_depart=models.DateTimeField(auto_now_add=True)
    date_arrive=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.id_assignation.id_voiture.nom_mt + ' ' + str(self.date_depart) + ' ' + str(self.date_arrive)
    
    
    
class Etudiant(models.Model):
    nom_etudiant=models.CharField(max_length=90,unique=True)
    lieu_naissance=models.CharField(max_length=30)
    date_naissance=models.CharField(max_length=10)
    matricule=models.CharField(max_length=10)
    promotion=models.CharField(max_length=120)
    class Meta:
        verbose_name='Etudiant'
        verbose_name_plural='Etudiants'
    def __str__(self) -> str:
        return self.nom_etudiant + ' ' + self.promotion
    
    
        


class Embarquation(models.Model):
    id_course=models.ForeignKey(Course,models.CASCADE)
    id_Etudiant=models.ForeignKey(Etudiant,models.CASCADE)
    date=models.DateField(auto_now_add=True)
    heure=models.TimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Embarquation'
        verbose_name_plural='Embarquations'
    def __str__(self) -> str:
        return  self.id_course.id_assignation.id_voiture.nom_mt + ' ' + str(self.date) + ' ' + str(self.heure) + ' ' + self.id_Etudiant.nom_etudiant
    
    
    
    
    