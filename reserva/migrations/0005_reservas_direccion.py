# Generated by Django 4.1.5 on 2023-01-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0004_alter_reservas_fecha_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='direccion',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]