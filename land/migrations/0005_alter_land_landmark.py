# Generated by Django 4.2.11 on 2024-04-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_land_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='landmark',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
