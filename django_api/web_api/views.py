from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import viewsets

# Create your views here.
from .models import Atendido, Responsavel, Escola, Matricula
from .serializers import AtendidoSerializer, ResponsavelSerializer, EscolaSerializer, MatriculaSerializer

class AtendidoViewSet(viewsets.ModelViewSet):
    queryset = Atendido.objects.all()
    serializer_class = AtendidoSerializer

class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer

class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

# class AlunoView(View):
    
#     queryset = Aluno.objects.all()

#     def get(self, request, *args, **kwargs):
#         # alunos = Aluno.objects.all()
#         # data = [
#         #     model_to_dict(aluno) for aluno in alunos
#         # ]
#         # response = {'data': data}
#         # return JsonResponse(response)
#         return self.list(request, )
    
#     def index(self, request, *args, **kwargs):
#         aluno = Aluno.objects.filter(id=self.kwargs['aluno_id'])
#         data = model_to_dict(aluno)
#         response = {'data': data}
#         return JsonResponse(response)

#     # def api_alunos(request):
#     #     alunos = Aluno.objects.all()
#     #     data = [
#     #         model_to_dict(aluno) for aluno in alunos
#     #     ]
#     #     response = {'data': data}
#     #     return JsonResponse(response)