# Generated by Django 3.2 on 2023-07-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil_desa_jarakan', '0002_auto_20230721_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecardimageplugin',
            name='tanggal',
            field=models.CharField(max_length=1000),
        ),
    ]
