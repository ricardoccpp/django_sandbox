from rest_framework import serializers
from .models import Atendido, Responsavel, Escola, Matricula

# Serializers define the API representation.
class AtendidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendido
        fields = '__all__'

class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'

class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'