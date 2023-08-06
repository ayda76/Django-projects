# Generated by Django 4.0.2 on 2023-08-06 17:54

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_color_remove_product_color_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='name',
            field=models.CharField(default='white', max_length=300),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]
