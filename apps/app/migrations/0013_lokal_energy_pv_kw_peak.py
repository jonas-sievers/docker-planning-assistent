# Generated by Django 3.2.6 on 2021-12-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_lokal_energy'),
    ]

    operations = [
        migrations.AddField(
            model_name='lokal_energy',
            name='pv_kw_peak',
            field=models.IntegerField(default=4),
        ),
    ]