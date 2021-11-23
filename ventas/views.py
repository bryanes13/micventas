from rest_framework import viewsets
from .models import *
from .serializer import *


# Create your views here.
class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializers

