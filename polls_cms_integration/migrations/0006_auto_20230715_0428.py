# Generated by Django 3.2 on 2023-07-15 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('polls_cms_integration', '0005_petalive'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetaLivePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='polls_cms_integration_petaliveplugin', serialize=False, to='cms.cmsplugin')),
                ('link', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.DeleteModel(
            name='PetaLive',
        ),
    ]
