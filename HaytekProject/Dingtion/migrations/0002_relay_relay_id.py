# Generated by Django 5.0.7 on 2024-07-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dingtion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relay',
            name='relay_id',
            field=models.IntegerField(null=True),
        ),
    ]
