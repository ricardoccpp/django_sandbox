from rest_framework import serializers
from .models import Aluno

# Serializers define the API representation.
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'sobrenome', 'idade']