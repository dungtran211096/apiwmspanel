# Generated by Django 2.1.2 on 2018-11-30 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_panelapi', '0004_remove_stream_id1'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='id_stream',
            field=models.CharField(default='', max_length=100),
        ),
    ]