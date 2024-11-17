from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Recurso(models.Model):
    nome = models.CharField(max_length=100)
    descricao =  models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ])
    criado_em = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.nome
    
class Profile(models.Model):
    cargo_choices = [
        ('CEO', 'CEO'),
        ('Gerente', 'Gerente | Mordomo'),
        ('Funcionario', 'Vilão'),
        ('Assistente', 'Assistente'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    codigo_recuperacao = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    cargo = models.CharField(max_length=100, choices=cargo_choices, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()