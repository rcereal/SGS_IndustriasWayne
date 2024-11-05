from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from .models import Recurso, Profile
from .forms import Form_do_Recurso


def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return  redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Usuario ou senha invalida.'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def lista_de_recursos(request):
    recursos = Recurso.objects.all()
    return render(request, 'lista_de_recursos.html',{'recursos': recursos})

@login_required
def adicionar_recurso(request):
    if request.method == 'POST':
        form = Form_do_Recurso(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_de_recursos')
    else:
        form = Form_do_Recurso()
        return render(request, 'adicionar_recurso.html',{'form': form})
    
@login_required
def editar_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, id=recurso_id)
    if request.method == 'POST':
        form = Form_do_Recurso(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect('lista_de_recursos')
    else:
        form = Form_do_Recurso(instance=recurso)
        return render(request, 'editar_recurso.html', {'form':form, 'recurso': recurso})
    
@login_required
def excluir_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, id=recurso_id)
    recurso.delete()
    return redirect('lista_de_recursos')

def solicitar_recuperacao_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            usuario = User.objects.get(email=email)
            codigo_recuperacao = get_random_string(20)
            usuario.profile.codigo_recuperacao = codigo_recuperacao
            usuario.profile.save()

            link = request.build_absolute_uri(
                reverse('redefinir_senha', args=[codigo_recuperacao])
            )
            send_mail(
                'Recuperação de Senha',
                f'Para redefinir sua senha, clique no link: {link}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )

            messages.success(request, 'Um email de recuperação de senha foi enviado.')
            return redirect('login')
        
        except User.DoesNotExist:
            messages.error(request, 'Email não encontrado')
        
    return render(request, 'solicitar_recuperacao_senha.html')

def redefinir_senha(request, codigo_recuperacao):
    try:
        usuario = User.objects.get(profile__codigo_recuperacao=codigo_recuperacao)
    except User.DoesNotExist:
        messages.error(request, 'Código de recuperação de senha inválido')
        return redirect('solicitar_recuperacao_senha')

    if request.method == 'POST':
        nova_senha = request.POST.get('nova_senha')
        nova_senha_confirmacao = request.POST.get('nova_senha_confirmacao')

        if nova_senha != nova_senha_confirmacao:
            messages.error(request, "As senhas não correspondem.")
            return render(request, 'redefinir_senha.html', {"codigo_recuperacao": codigo_recuperacao})

        usuario.set_password(nova_senha)
        usuario.profile.codigo_recuperacao = ''
        usuario.save()
        messages.success(request, 'Sua senha foi redefinida com sucesso.')
        return redirect('login')

    return render(request, 'redefinir_senha.html', {"codigo_recuperacao": codigo_recuperacao})

@user_passes_test(lambda u: u.is_staff)
def gerenciar_usuario(request, user_id=None):
    usuario = None

    if user_id:
        usuario = get_object_or_404(User, id=user_id)
    else:
        usuario = None

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        cargo = request.POST.get('cargo')

        # Atualizar usuário
        if usuario:
            usuario.username = username
            usuario.email = email
            if senha:
                usuario.set_password(senha)  # Atualiza a senha se fornecida
            usuario.save()

            # Atualiza o perfil do usuário (campo cargo)
            if usuario.profile:
                usuario.profile.cargo = cargo
                usuario.profile.save()
            else:
                # Caso o perfil não exista, criamos um novo
                Profile.objects.create(user=usuario, cargo=cargo)

            messages.success(request, 'Usuário atualizado com sucesso.')

        # Criar novo usuário
        else:
            usuario = User.objects.create_user(username=username, email=email, password=senha)
            Profile.objects.create(user=usuario, cargo=cargo)  # Criar o perfil junto com o usuário
            messages.success(request, 'Usuário criado com sucesso.')

        return redirect('lista_de_usuarios')  # Redireciona para a lista de usuários após a criação/atualização

    return render(request, 'gerenciar_usuario.html', {"usuario": usuario})