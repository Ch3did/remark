from datetime import datetime

from django.db import models

DECLARACAO_PADRAO = (
    "Declaramos que foi realizado o serviço de gravação com os caracteres VIS..."
)


class LaudoVidros(models.Model):
    tipo_servico = models.CharField(
        max_length=25, default="Gravação de Vidros", verbose_name="Tipo de Serviço"
    )
    num_original = models.CharField(
        max_length=25, blank=True, verbose_name="Número Original"
    )
    data_aplicacao = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Data de Aplicação"
    )
    data_emissao = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Data de Emissão"
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
    descricao_foto_3 = models.CharField(
        max_length=20, blank=True, verbose_name="Descrição da Foto 3"
    )
    foto_3 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Foto 3"
    )
    descricao_foto_4 = models.CharField(
        max_length=20, blank=True, verbose_name="Decrição da Foto 4"
    )
    foto_4 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Foto 4"
    )
    descricao_foto_5 = models.CharField(
        max_length=20, blank=True, verbose_name="Descrição da Foto 5"
    )
    foto_5 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Foto 5"
    )
    descricao_foto_6 = models.CharField(
        max_length=20, blank=True, verbose_name="Descrição da Foto 6"
    )
    foto_6 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Foto 6"
    )
    descricao_foto_7 = models.CharField(
        max_length=20, blank=True, verbose_name="Descrição da Foto 7"
    )
    foto_7 = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Foto 7"
    )
    indicacao = models.BooleanField(default=False, verbose_name="Veio por Indicação")
    valor_servico = models.IntegerField(blank=False, verbose_name="Valor Cobrado")

    class Meta:
        verbose_name_plural = "Laudos de  Vidros"

    def __str__(self):
        return str(self.placa)
