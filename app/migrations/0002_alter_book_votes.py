# Generated by Django 4.1.13 on 2024-04-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='votes',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
