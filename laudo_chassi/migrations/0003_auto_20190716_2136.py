# Generated by Django 2.2.3 on 2019-07-17 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laudo_chassi', '0002_laudochassi_decalque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laudochassi',
            name='declaracao_de_servico',
            field=models.TextField(blank=True, default='Declaramos que foi realizado o serviço de Remarcação do Chassi com os caracteres...\nDeclaramos que foi realizado o serviço de 2ª Gravação da numeração do Chassi com os caracteres...\nDeclaramos que foi realizado o serviço de Gravação da numeração do Chassi com os caracteres...', max_length=300),
        ),
    ]
