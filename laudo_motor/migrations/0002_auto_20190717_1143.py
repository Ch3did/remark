# Generated by Django 2.2.3 on 2019-07-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("laudo_motor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="laudomotor",
            name="tipo_servico",
            field=models.CharField(default="Gravação de Motor", max_length=30),
        ),
    ]
