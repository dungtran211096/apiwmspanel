# Generated by Django 2.1.2 on 2018-12-03 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vega1', '0006_re_publish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'ordering': ('name',), 'verbose_name': 'server', 'verbose_name_plural': 'servers'},
        ),
    ]