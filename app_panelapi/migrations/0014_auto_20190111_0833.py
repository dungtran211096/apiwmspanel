# Generated by Django 2.1.2 on 2019-01-11 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_panelapi', '0013_re_publish1_server1_server_id1_stream1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='re_publish1',
        ),
        migrations.DeleteModel(
            name='server1',
        ),
        migrations.DeleteModel(
            name='server_id1',
        ),
        migrations.DeleteModel(
            name='stream1',
        ),
    ]
