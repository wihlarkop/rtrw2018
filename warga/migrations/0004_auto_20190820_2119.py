# Generated by Django 2.2.2 on 2019-08-20 14:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('warga', '0003_auto_20190813_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='kk',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 8, 20, 14, 19, 21, 711617, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kk',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ktp',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 8, 20, 14, 19, 28, 143546, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ktp',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Ktpkk',
        ),
    ]
