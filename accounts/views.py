from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.ERROR(request, 'Usuário ou senha inválidos')
        return render(request, 'accounts/login.html')

    else:
        auth.login(request,user)
        messages.success(request, 'Aproveite :)')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    senha = request.POST.get('senha')
    confirmarsenha = request.POST.get('confirmarsenha')
    email = request.POST.get('email')
    celular = request.POST.get('celular')
    apelido = request.POST.get('apelido')
    preparado = request.POST.get('preparado')

   # try:
    #    validate_email(email)
    #except:
     #   messages.error(request, 'E-mail inválido')
     #   return render(request, 'accounts/register.html')

    if len(senha) < 6:
        messages.error(request, 'Senha curta demais :(')
        return render(request, 'accounts/register.html')

    #if senha != confirmarsenha:
    #    messages.error(request, 'Senhas não são iguais, será que esqueceu de algo?')
     #   return render(request, 'accounts/register.html')

    if User.objects.filter(username=email).exists():
        messages.error(request, 'Esse e-mail já existe, esqueceu sua conta?')
        return render(request, 'accounts/register.html')

    user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Ops, ocorreu um erro...')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, 'Contato foi salvo com sucesso!')
    return redirect('dashboard')

    #descricao = request.POST.get('descrica')  <-- posso usar para validar os campos na unha