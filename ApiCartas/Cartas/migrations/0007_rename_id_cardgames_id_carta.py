# Generated by Django 4.2.3 on 2023-09-13 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cartas', '0006_cardgames_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardgames',
            old_name='id',
            new_name='id_carta',
        ),
    ]