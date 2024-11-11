from .models import Profile

def check_cargo(user, required_cargo):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.cargo in required_cargo or user.is_staff