from django.contrib import admin

# Register your models here.
from .models import Atendido, Responsavel, Escola

admin.site.register(Escola)
admin.site.register(Atendido)
admin.site.register(Responsavel)