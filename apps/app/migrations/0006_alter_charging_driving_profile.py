# Generated by Django 3.2.6 on 2021-12-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_charging_cable_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charging',
            name='driving_profile',
            field=models.CharField(choices=[('20', '20 km/Tag'), ('40', '40 km/Tag'), ('60', '60 km/Tag'), ('100', '100 km/Tag')], default='40', max_length=200),
        ),
    ]
