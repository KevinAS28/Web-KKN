# Generated by Django 3.2 on 2023-07-21 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_cms_integration', '0006_auto_20230715_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecardimage',
            name='tanggal',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
