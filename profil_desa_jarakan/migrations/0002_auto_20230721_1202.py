# Generated by Django 3.2 on 2023-07-21 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil_desa_jarakan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homecardimageplugin',
            name='link_detail',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homecardimage',
            name='tanggal',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='homecardimageplugin',
            name='tanggal',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
