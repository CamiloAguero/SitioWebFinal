# Generated by Django 4.1.5 on 2023-01-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0006_ficha_imagen2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='observacion',
            field=models.TextField(verbose_name='Observaciones'),
        ),
    ]
