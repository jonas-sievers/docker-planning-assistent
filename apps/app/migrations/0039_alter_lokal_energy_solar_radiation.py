# Generated by Django 3.2.6 on 2022-01-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20220115_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokal_energy',
            name='solar_radiation',
            field=models.CharField(choices=[('950', '950'), ('1000', '1000'), ('1050', '1050'), ('1100', '1100'), ('1150', '1150')], default=None, max_length=200),
        ),
    ]
