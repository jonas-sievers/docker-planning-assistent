# Generated by Django 3.2.6 on 2022-01-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20220112_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokal_energy',
            name='roof_size',
            field=models.CharField(choices=[('7', '7 $m^{2}$'), ('14', '14 $m^{2}$'), ('20', '20 $m^{2}$'), ('30', '30 m^2^'), ('40', '40 m^2^'), ('50', '50 m^2^'), ('60', '60 m^2^')], default=None, max_length=200),
        ),
    ]
