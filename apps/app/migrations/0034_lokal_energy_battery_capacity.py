# Generated by Django 3.2.6 on 2022-01-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20220114_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='lokal_energy',
            name='battery_capacity',
            field=models.CharField(choices=[('1', '1'), ('3', '3'), ('5', '5'), ('7', '7'), ('10', '10'), ('14', '14')], default='1', max_length=200),
        ),
    ]