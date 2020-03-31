from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Rest Framework
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class index(View):
    def get(self, request, *args, **kwargs):
        context = {
            "Tesla" : "Nikola Tesla - Genio por Excelencia"
        }
        return render(request, "index.html", context)


class VisualizadorJSON(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        from random import sample
        cientificos = ['Nikola Tesla', 'Isaac Newton', 'Nicolas Copernico', 'Maria Curie', 'Arquimedes', 'Erwin Schrödinger']
        lista = list(range(80))
        puntos = sample(lista, 6)
        # puntos = [50, 19, 3, 5, 2, 3]
        datos = {
                "labels": puntos,
                "cientificos": cientificos
        }
        return Response(datos)
