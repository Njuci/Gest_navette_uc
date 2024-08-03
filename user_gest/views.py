from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

class UtilisateurListCreate(APIView):
    def get(self,request):
        utilisateur=Utilisateur.objects.all()
        serializer=UtilisateurSerializer(utilisateur,many=True)
        return Response(serializer.data)
    
    def put(self,request):
        serializer=UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
     
    
    def post(self,request):
        serializer=UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class UtilisateurRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Utilisateur.objects.all()
    serializer_class=UtilisateurSerializer