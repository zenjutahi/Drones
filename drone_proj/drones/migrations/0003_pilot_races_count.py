# Generated by Django 3.0.3 on 2020-02-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0002_auto_20200224_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilot',
            name='races_count',
            field=models.IntegerField(default=0),
        ),
    ]
