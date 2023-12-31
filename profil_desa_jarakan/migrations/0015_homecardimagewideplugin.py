# Generated by Django 3.2 on 2023-08-01 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('profil_desa_jarakan', '0014_imageresponsiveplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCardImageWidePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='profil_desa_jarakan_homecardimagewideplugin', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('detail', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
