# Generated by Django 3.2 on 2023-07-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_cms_integration', '0007_homecardimageplugin_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='homecardimageplugin',
            name='tanggal',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
