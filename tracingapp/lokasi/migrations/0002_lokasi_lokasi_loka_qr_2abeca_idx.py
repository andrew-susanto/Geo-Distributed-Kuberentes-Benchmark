# Generated by Django 4.0 on 2022-03-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lokasi', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='lokasi',
            index=models.Index(fields=['qr'], name='lokasi_loka_qr_2abeca_idx'),
        ),
    ]
