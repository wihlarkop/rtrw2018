# Generated by Django 2.2.2 on 2019-08-13 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warga', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ktpkk',
            name='is_kepala_keluarga',
        ),
        migrations.AddField(
            model_name='kk',
            name='is_kepala_keluarga',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='kk',
            name='nik',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='warga.Ktp'),
            preserve_default=False,
        ),
    ]