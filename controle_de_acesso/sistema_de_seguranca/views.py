from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Recurso
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
