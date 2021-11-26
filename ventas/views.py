from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
# Create your views here.
class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializers


class ClienteViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Ventas.objects.all()
        serializer_class = VentasSerializers(queryset, many=True)
        return Response(serializer_class.data)
    def retrieve(self, request, pk=None):
        queryset = Ventas.objects.filter(cedula_cliente=pk)
        serializer = VentasSerializers(queryset, many=True)
        return Response(serializer.data)
