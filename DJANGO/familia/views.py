from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from familia.models import Familia


def save_family(request):

    template1 = loader.get_template('prueba.html')

    render1 = template1.render({})

    return HttpResponse(render1)

def family(request):
    
    template = loader.get_template('familia.html')
    
    family_member = Familia.objects.all()
    
    render = template.render({'lista_familia':family_member})
    
    return HttpResponse(render)
    