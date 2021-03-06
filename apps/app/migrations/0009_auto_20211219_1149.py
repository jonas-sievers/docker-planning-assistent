# Generated by Django 3.2.6 on 2021-12-19 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_charging_usage_years'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Charging',
        ),
        migrations.AddField(
            model_name='real_estate',
            name='cable_length',
            field=models.CharField(choices=[('10', '10 m'), ('20', '20 m'), ('30', '30 m'), ('40', '40 m'), ('50', '50 m'), ('100', '100 m'), ('200', '200 m')], default='10', max_length=200),
        ),
        migrations.AddField(
            model_name='real_estate',
            name='driving_profile',
            field=models.CharField(choices=[('20', '20 km/Tag'), ('40', '40 km/Tag'), ('60', '60 km/Tag'), ('100', '100 km/Tag')], default='40', max_length=200),
        ),
        migrations.AddField(
            model_name='real_estate',
            name='usage_years',
            field=models.CharField(choices=[('10', '10 Jahre'), ('20', '20 Jahre'), ('30', '30 Jahre'), ('40', '40 Jahre')], default='20', max_length=200),
        ),
    ]
