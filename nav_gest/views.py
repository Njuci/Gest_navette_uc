from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course,Assigner_Voiture,Moyen_Transport,Etudiant,Embarquation
from .serializers import CourseSerializer,Assigner_VoitureSerializer,Moyen_TransportSerializer,EtudiantSerializer,EmbarquationSerializer

class CoursesList(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        return Response(serializer.data)
    # get course by id of user
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CoursesList_User(APIView):        
    def get(self, request, pk):
        courses = Course.objects.filter(id_assignation__id_user=pk)
        serializer = CourseSerializer(courses, many=True)
        liste_courses = []
        
        if not serializer.data:
            return Response(status=status.HTTP_204_NO_CONTENT)
        for course in serializer.data:
            dict_course = {}
            id_assignation = Assigner_Voiture.objects.get(id=course['id_assignation'])
            assigne=Assigner_VoitureSerializer(id_assignation)
            id_voiture = assigne.data['id_voiture']
          
            voitures = Moyen_Transport.objects.get(id=id_voiture) 
            dict_course['voiture'] = voitures.nom_mt
            # convert datetime to date le mettre dans le format jj/mm/aaaa
            dict_course['date'] = course['date_depart'].split('T')[0].split('-')[2] + '/' + course['date_depart'].split('T')[0].split('-')[1] + '/' + course['date_depart'].split('T')[0].split('-')[0]
            dict_course['carburant'] = course['carburant']
            if course['nombre_passager'] == 0:
                # If the number of passengers is zero, find the number of embarkations for this course
                Embarquations = Embarquation.objects.filter(id_course=course['id'])
                serial_embarqua=EmbarquationSerializer(Embarquations,many=True)
                print(serial_embarqua.data)
                print(len(Embarquations))
                # Set the number of passengers to the number of embarkations
                dict_course['nombre_passager'] = len(Embarquations)
            else:
                # If the number of passengers is not zero, use the existing number of passengers
                dict_course['nombre_passager'] = course['nombre_passager']
                        
            liste_courses.append(dict_course)
        
        return Response(liste_courses, status=status.HTTP_200_OK)

class Assigner_VoituresList(APIView):
    def get(self,request):
        assigner_voitures = Assigner_Voiture.objects.all()
        serializer = Assigner_VoitureSerializer(assigner_voitures,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Assigner_VoitureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        serializer = Assigner_VoitureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        serializer = Assigner_VoitureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#get assognation by id of user  
class AssignationList(APIView):
    def get(self, request, user_id):
        # la derniere assignation à une voiture donnée pour un user 
                
        assignations = Assigner_Voiture.objects.filter(id_user=user_id)
        serializer = Assigner_VoitureSerializer(assignations, many=True)
    
        liste_assignation=[]
        if not serializer.data:
            return Response(status=status.HTTP_204_NO_CONTENT)
        for assignation in serializer.data:
            dict_assign={}
            voiture=Moyen_Transport.objects.get(id=assignation['id_voiture'])
            dict_assign['id']=assignation['id']
            dict_assign['voiture']=voiture.nom_mt
            dict_assign['date']=assignation['date_ass']
            liste_assignation.append(dict_assign)
            
        
        return Response(liste_assignation, status=status.HTTP_200_OK)





class Moyen_TransportsList(APIView):
    def get(self,request):
        moyen_transports = Moyen_Transport.objects.all()
        serializer = Moyen_TransportSerializer(moyen_transports,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = Moyen_TransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        serializer = Moyen_TransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        serializer = Moyen_TransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class EtudiantsList(APIView):
    def get(self,request):
        etudiants = Etudiant.objects.all()
        serializer = EtudiantSerializer(etudiants,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = EtudiantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        serializer = EtudiantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        serializer = EtudiantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class EmbarquationsList(APIView):
    def get(self,request):
        embarquations = Embarquation.objects.all()
        serializer = EmbarquationSerializer(embarquations,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = EmbarquationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        serializer = EmbarquationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        serializer = EmbarquationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)