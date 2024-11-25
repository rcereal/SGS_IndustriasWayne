from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Recurso(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

def validate_image(image):
    file_size = image.file.size
    limit = 5 * 1024 * 1024
    if file_size > limit:
        raise ValidationError("A imagem não pode ser maior que 5MB.")
    if not image.name.endswith(('jpg', 'jpeg', 'png', 'gif')):
        raise ValidationError("Formato de imagem não suportado.")

class Profile(models.Model):
    CARGO_CHOICES = [
        ('CEO', 'CEO'),
        ('Gerente', 'Gerente'),
        ('Funcionario', 'Funcionário'),
        ('Assistente', 'Assistente'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', unique=True)
    codigo_recuperacao = models.CharField(max_length=20, blank=True)
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
