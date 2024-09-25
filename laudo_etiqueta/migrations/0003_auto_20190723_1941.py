# Generated by Django 2.2.3 on 2019-07-23 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laudo_etiqueta', '0002_auto_20190716_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laudoetiqueta',
            options={'verbose_name_plural': 'Laudos de Etiqueta'},
        ),
        migrations.AlterField(
            model_name='laudoetiqueta',
            name='cpf',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='laudoetiqueta',
            name='estado_veiculo',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='laudoetiqueta',
            name='marca',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='laudoetiqueta',
            name='modelo',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='laudoetiqueta',
            name='num_chassi',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='laudoetiqueta',
            name='tipo_servico',
            field=models.CharField(default='Etiqueta', max_length=25),
        ),
    ]
