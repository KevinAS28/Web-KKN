# Generated by Django 3.2 on 2023-07-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil_desa_jarakan', '0011_profilartikelplugin_profilgaleriplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilartikelplugin',
            name='deskripsi',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
