# Generated by Django 3.2 on 2023-07-30 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('profil_desa_jarakan', '0013_perangkatdesaplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageResponsivePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='profil_desa_jarakan_imageresponsiveplugin', serialize=False, to='cms.cmsplugin')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
