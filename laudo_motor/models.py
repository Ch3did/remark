from datetime import datetime

from django.db import models

DECLARACAO_PADRAO = "Declaramos que foi realizado o serviço de Remarcação do motor com os caracteres...\n"
DECLARACAO_PADRAO += (
    "Declaramos que foi realizado o serviço de Gravação do motor com os caracteres..."
)


class LaudoMotor(models.Model):
    tipo_servico = models.CharField(
        max_length=25, default="Gravação de Motor", verbose_name="Tipo de Serviço"
    )
    num_motor = models.CharField(
        max_length=25, blank=True, verbose_name="Número do Motor"
    )
    data_realizacao = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Data de Realização"
    )
    data_emissao = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Data de Emissão"
    )
    responsavel = models.CharField(
        max_length=40, blank=True, verbose_name="Responsável"
    )
    num_autorizacao = models.CharField(
        max_length=15, blank=True, verbose_name="Número da Autorização"
    )
    cidade_autorizacao = models.CharField(
        max_length=30, blank=True, verbose_name="Cidade da Autorização"
    )
    estado_autorizacao = models.CharField(
        max_length=2, blank=True, verbose_name="Estado da Autorização"
    )
    marca = models.CharField(max_length=25, blank=True, verbose_name="Marca do Veículo")
    modelo = models.CharField(
        max_length=25, blank=False, verbose_name="Modelo do Veículo"
    )
    ano_veiculo = models.IntegerField(blank=False, verbose_name="Ano do Veículo")
    ano_modelo = models.IntegerField(blank=False, verbose_name="Ano do Modelo")
    placa = models.CharField(max_length=10, blank=True, verbose_name="Placa do Veículo")
    cidade_veiculo = models.CharField(
        max_length=30, blank=True, verbose_name="Cidade do Veículo"
    )
    estado_veiculo = models.CharField(
        max_length=2, blank=True, verbose_name="Estado do Veículo"
    )
    nome = models.CharField(
        max_length=40, blank=True, verbose_name="Nome do Proprietário"
    )
    cpf = models.CharField(
        max_length=15, blank=True, verbose_name="CPF do Proprietário"
    )
    declaracao_de_servico = models.TextField(
        max_length=300,
        blank=True,
        default=DECLARACAO_PADRAO,
        verbose_name="Declaração de Serviço",
    )
    descricao_foto_1 = models.CharField(
        max_length=20, blank=True, verbose_name="Descrição da Foto 1"
    )
    foto_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Foto 1")
    descricao_foto_2 = models.CharField(
        max_length=20, blank=True, verbose_name="Descrição da Foto 2"
    )
    foto_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Foto 2")
    indicacao = models.BooleanField(default=False, verbose_name="Veio por Indicacao")
    decalque = models.BooleanField(default=False, verbose_name="Tem Decalque")
    valor_servico = models.IntegerField(blank=False, verbose_name="Valor Cobrado")

    class Meta:
        verbose_name_plural = "Laudos de Motor"

    def __str__(self):
        return str(self.placa)
