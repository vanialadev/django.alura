from django.shortcuts import render
from models import Perfil


def index(request):
    return render(request, 'index.html')


def exibir(request, perfil_id):
    perfil = Perfil()
    if perfil_id == '1':
        perfil = Perfil('Flavio Almeida', 'xxxxxxx', '777777', 'Caelum')
    if perfil_id == '2':
        perfil = Perfil('Romulo Henrique', 'R@R.com', '888888', 'Caelum')

    return render(request, 'perfil.html', {"perfil": perfil})
