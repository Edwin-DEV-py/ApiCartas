# Generated by Django 4.2.3 on 2023-09-18 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartas', '0007_rename_id_cardgames_id_carta'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='discount',
            field=models.BooleanField(default=False),
        ),
    ]
