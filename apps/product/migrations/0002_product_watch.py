# Generated by Django 4.0.4 on 2022-05-31 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='watch',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
