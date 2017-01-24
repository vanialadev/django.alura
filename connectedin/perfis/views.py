from django.contrib.auth.decorators import login_required
from django.template import loader
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from models import Perfil, Convite


@require_http_methods(["GET"])
@login_required
def index(request):
    print request.user.username
    print request.user.email
    print request.user.has_perm('perfis.add_convite')
    if not request.user.has_perm('perfis.add_convite'):
        return render(request, 'template_com_msg_de_erro.html')
        # return HttpResponseForbidden('Acesso negado')
        # return render(request, 'template_com_msg_de_erro.html')

    return render(request, 'index.html', {'perfis': Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})


@login_required
def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    return render(request, 'perfil.html', {"perfil": perfil, "perfil_logado": get_perfil_logado(request), 'ja_eh_contato': ja_eh_contato})


permission_required('perfis.add_convite', raise_exception=True)
@login_required
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    # return render(request, 'index.html', {'perfis' : Perfil.objects.all()})
    return redirect('index')


@login_required
def get_perfil_logado(request):
    return request.user.perfil


@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')
