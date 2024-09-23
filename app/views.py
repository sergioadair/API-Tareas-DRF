from rest_framework import viewsets
from .serializer import TareaSerializer
from .models import Tarea

# Create your views here.
class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer