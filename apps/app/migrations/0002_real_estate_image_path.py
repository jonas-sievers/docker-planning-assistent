# Generated by Django 3.2.6 on 2021-12-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='real_estate',
            name='image_path',
            field=models.CharField(default='', max_length=200),
        ),
    ]