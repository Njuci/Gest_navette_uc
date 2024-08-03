from rest_framework.serializers import ModelSerializer
from .models import Moyen_Transport,Assigner_Voiture,Course,Etudiant,Embarquation

class Moyen_TransportSerializer(ModelSerializer):
    class Meta:
        model=Moyen_Transport
        fields='__all__'
class Assigner_VoitureSerializer(ModelSerializer):
    class Meta:
        model=Assigner_Voiture
        fields='__all__'
        
class CourseSerializer(ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        
class EtudiantSerializer(ModelSerializer):
    class Meta:
        model=Etudiant
        fields='__all__'
        
class EmbarquationSerializer(ModelSerializer):
    class Meta:
        model=Embarquation
        fields='__all__'
        
        
