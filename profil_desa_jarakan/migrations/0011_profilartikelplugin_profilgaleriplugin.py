# Generated by Django 3.2 on 2023-07-29 13:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('profil_desa_jarakan', '0010_wisataplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilArtikelPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='profil_desa_jarakan_profilartikelplugin', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('tanggal', models.DateField(default=datetime.date.today)),
                ('link', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ProfilGaleriPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='profil_desa_jarakan_profilgaleriplugin', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('tanggal', models.DateField(default=datetime.date.today)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
