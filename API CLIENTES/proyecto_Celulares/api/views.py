from urllib import response
from django.http.response import JsonResponse
from django.views import View
from .models import Celulares
from django.utils.decorators import method_decorator # estos dos se usan para no tener que hacer la validacion
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CelularesSerialiezer
# Create your views here.
# se crea el get, post, put y delate



class CelularesView(View):
    
    @method_decorator(csrf_exempt) # saltar validacion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    #buscar
    def get(self,request,id=0):
        if (id>0):
            clientes=list(Celulares.objects.filter(id=id).values())
            if len(clientes)>0:
                cliente=clientes[0]
                datos={'message':"hecho",'clientes':clientes}
            else:
                datos={'message':"Cliente no encontrado"}
            return JsonResponse(datos)
        else:
            clientes= list(Celulares.objects.values())
            if len(clientes)>0:
                datos={'message':"hecho",'clientes':clientes}
            else:
                datos={'message':"Cliente no encontrado"}
            return JsonResponse(datos)
    #agregar
    def post(self,request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Celulares.objects.create(identificación=jd['identificación'],númeroDeProductosVendidos=jd['númeroDeProductosVendidos'])
        datos={'message':"hecho"}
        return JsonResponse(datos)
    #actualizar
    def put(self,request,id):
        jd = json.loads(request.body)
        clientes=list(Celulares.objects.filter(id=id).values())
        if len(clientes)>0:
            cliente=Celulares.objects.get(id=id)
            cliente.identificación=jd['identificación']
            cliente.númeroDeProductosVendidos=jd['número De Productos Vendidos']
            cliente.save()
            datos={'message':"hecho"}
        else:
            datos={'message':"Cliente no encontrado"}
        return JsonResponse(datos)
    #eliminar
    def delete(self,request,id):
        clientes=list(Celulares.objects.filter(id=id).values())
        if len(clientes)>0:
            Celulares.objects.filter(id=id).delete()
            datos={'message':"hecho"}
        else:
            datos={'message':"Cliente no encontrado"}
        return JsonResponse(datos)