# Generated by Django 4.2.3 on 2023-09-20 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartas', '0008_card_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]