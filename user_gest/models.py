from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.




from django.contrib.auth.models import Group,Permission


class Utilisateur(AbstractUser):
    USER_TYPE_CHOICES = (
           ('cf', 'Chauffeur'),
           ('ST', 'Service de Transport'),
       )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    USERNAME_FIELD='username'
    groups = models.ManyToManyField(Group, related_name='utilisateur_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='utilisateur_set', blank=True
    )
    
    photo=models.ImageField(upload_to='photo_profile',blank=True)
    def has_perm(self,perms):
        return True
    def has_module_perms(self,app_label):
        return True 
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'