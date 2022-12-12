from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import viewsets

# Create your views here.
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoView(View):
    
    queryset = Aluno.objects.all()

    def get(self, request, *args, **kwargs):
        # alunos = Aluno.objects.all()
        # data = [
        #     model_to_dict(aluno) for aluno in alunos
        # ]
        # response = {'data': data}
        # return JsonResponse(response)
        return self.list(request, )
    
    def index(self, request, *args, **kwargs):
        aluno = Aluno.objects.filter(id=self.kwargs['aluno_id'])
        data = model_to_dict(aluno)
        response = {'data': data}
        return JsonResponse(response)

    # def api_alunos(request):
    #     alunos = Aluno.objects.all()
    #     data = [
    #         model_to_dict(aluno) for aluno in alunos
    #     ]
    #     response = {'data': data}
    #     return JsonResponse(response)