from .models import Profile

def check_cargo(user, cargos_validos):
    try:
        return user.profile.cargo in cargos_validos  # Certifique-se de que o perfil está sendo acessado
    except user.profile.DoesNotExist:
        return False