# Generated by Django 4.0 on 2022-01-04 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pengguna', '0001_initial'),
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='pengguna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengguna.pengguna'),
        ),
    ]