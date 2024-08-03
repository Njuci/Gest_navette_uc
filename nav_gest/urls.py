from django.urls import path

from .views import CoursesList,Assigner_VoituresList,Moyen_TransportsList,EtudiantsList,EmbarquationsList,CoursesList_User,AssignationList


urlpatterns = [
    path('moyen_transports/', Moyen_TransportsList.as_view(), name='moyen_transports'),
    path('assigner_voitures/', Assigner_VoituresList.as_view(), name='assigner_voitures'),
    path('assignations/<int:user_id>/', AssignationList.as_view(), name='assignation'),
    path('courses/<int:pk>/', CoursesList_User.as_view(), name='courses_user'),
    path('course_list/', CoursesList.as_view(), name='courses'),
    path('etudiants/', EtudiantsList.as_view(), name='etudiants'),
    path('embarquations/', EmbarquationsList.as_view(), name='embarquations'),
]
