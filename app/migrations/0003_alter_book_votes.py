# Generated by Django 4.1.13 on 2024-04-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_book_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='votes',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
