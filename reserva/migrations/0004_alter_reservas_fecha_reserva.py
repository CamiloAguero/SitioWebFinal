# Generated by Django 4.1.5 on 2023-01-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0003_alter_reservas_options_alter_reservas_fecha_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='fecha_reserva',
            field=models.DateField(),
        ),
    ]