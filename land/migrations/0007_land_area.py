# Generated by Django 4.2.11 on 2024-04-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0006_remove_land_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='area',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
