# Generated by Django 5.0.6 on 2024-07-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dingtion', '0003_alter_device_options_alter_relay_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relay',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relay',
            name='type',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
