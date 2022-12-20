from django.db import models
from django.utils import timezone 

# Create your models here.
class Escola(models.Model):
    nome = models.CharField(max_length=200, blank=False, default='')
    cep = models.CharField(max_length=8, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    numero_endereco = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    bairro = models.CharField(max_length=200, blank=True, null=True)
    cidade = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    cpf = models.CharField(max_length=12, unique=True, blank=False, default='00000000000')
    nome = models.CharField(max_length=200, blank=False, default='')
    GENEROS = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('nao_binario', 'Não Binário')
    )
    genero = models.CharField(max_length=20, blank=False, choices=GENEROS, null=True)
    data_nascimento = models.DateField(blank=False, default=timezone.now)
    nome_mae = models.CharField(max_length=200, blank=True, null=True)
    nome_pai = models.CharField(max_length=200, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    numero_endereco = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    bairro = models.CharField(max_length=200, blank=True, null=True)
    celular = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['nome']    

class Responsavel(Pessoa):
    telefone = models.CharField(max_length=200, blank=True, null=True)
    telefone_comercial = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.nome} ({self.cpf})'

class Atendido(Pessoa):
    PERIODOS = (
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
        ('integral', 'Integral')
    )
    escola = models.ForeignKey(
        Escola,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    periodo_escolar = models.CharField(max_length=10, choices=PERIODOS, null=True)
    autorizado_embora_sozinho = models.BooleanField(default=False)
    autorizado_buscar_01 = models.CharField(max_length=200, blank=False, default='')
    autorizado_buscar_02 = models.CharField(max_length=200, blank=False, default='')
    autorizado_buscar_03 = models.CharField(max_length=200, blank=False, default='')
    autorizado_buscar_04 = models.CharField(max_length=200, blank=False, default='')
    problema_saude = models.BooleanField(default=False)
    problema_saude_detalhe = models.TextField(blank=True, default='')
    uso_medicamento = models.BooleanField(default=False)
    uso_medicamento_detalhe = models.TextField(blank=True, default='')
    alergia = models.BooleanField(default=False)
    alergia_detalhe = models.TextField(blank=True, default='')
    auxilio_governo = models.BooleanField(default=False)
    auxilio_governo_valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ajuda_mensal = models.BooleanField(default=False)
    ajuda_mensal_detalhe = models.TextField(blank=True, default='')
    ajuda_mensal_valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    renda_per_capita = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pais_moram_juntos = models.BooleanField(default=False)
    situacao_pais = models.CharField(max_length=200, blank=False, default='')
    quantidade_residentes = models.IntegerField(blank=False, default=1)
    residente_assalariado = models.BooleanField(default=False)
    quantidade_residentes_assalariados = models.IntegerField(blank=False, default=1)
    ocupacao_pai = models.CharField(max_length=200, blank=True, default='')
    salario_pai = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ocupacao_mae = models.CharField(max_length=200, blank=True, default='')
    salario_mae = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ocupacao_outros = models.CharField(max_length=200, blank=True, default='')
    salario_outros = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    trauma = models.BooleanField(default=False)
    responsavel = models.ForeignKey(
        Responsavel, 
        on_delete=models.CASCADE,
        blank=True
    )
    parentesco_responsavel = models.CharField(max_length=200, blank=False, null=True)
    STATUS = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('desligado', 'Desligado')
    )
    status = models.CharField(max_length=10, choices=STATUS, null=True)
    motivo_status = models.TextField(blank=True, default='')
    numero_nis = models.CharField(max_length=20, blank=True, default='')
    numero_sus = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    atendido = models.ForeignKey(
        Atendido,
        on_delete=models.CASCADE
    )
    data_inicio = models.DateField(blank=False)
    PERIODOS = (
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
        ('integral', 'Integral')
    )
    periodo = models.CharField(max_length=10, choices=PERIODOS, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    models.UniqueConstraint(
        name='unique_matricula',
        fields=['atendido', 'data_inicio']
    )

    def __str__(self):
        return self.pk