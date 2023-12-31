# Generated by Django 3.2 on 2023-07-16 16:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACardPluginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HomeCardImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tanggal', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='HomeCardImagePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='profil_desa_jarakan_homecardimageplugin', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(max_length=100)),
                ('tanggal', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PejabatCardPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='profil_desa_jarakan_pejabatcardplugin', serialize=False, to='cms.cmsplugin')),
                ('tingkat_jabatan', models.CharField(max_length=100)),
                ('nama_pejabat', models.CharField(max_length=100)),
                ('tanggal_mulai_menjabat', models.DateField(default=datetime.date.today)),
                ('tanggal_akhir_jabatan', models.DateField(default=datetime.date.today)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PetaLivePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='profil_desa_jarakan_petaliveplugin', serialize=False, to='cms.cmsplugin')),
                ('link', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SmallGalleryPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='profil_desa_jarakan_smallgalleryplugin', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
