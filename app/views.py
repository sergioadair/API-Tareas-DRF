from rest_framework import serializers, viewsets
from .models import Tarea

# Create your views here.
class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()

    class Serializer(serializers.ModelSerializer):
        class Meta:
            model = Tarea
            fields = '__all__'
    serializer_class = Serializer