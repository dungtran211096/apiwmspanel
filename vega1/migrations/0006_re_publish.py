# Generated by Django 2.1.2 on 2018-12-03 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vega1', '0005_stream_id_stream'),
    ]

    operations = [
        migrations.CreateModel(
            name='re_publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_rule', models.CharField(default='', max_length=100)),
                ('src_strm', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
