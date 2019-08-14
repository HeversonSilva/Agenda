from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        listado=True
    )
    paginator = Paginator(contatos, 10)
    #  faz a paginação da lista chamada contato

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def contato(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.listado:
        raise Http404()

    return render(request, 'contatos/contato.html', {
        'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(''), 'sobrenome')

    if termo is None or not termo:
        messages.add_message(
            request, messages.WARNING, 'O campo não pode ser vazio!'
        )
        return redirect('index')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo)
    )
    paginator = Paginator(contatos, 10)
    #  faz a paginação da lista chamada contato

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
