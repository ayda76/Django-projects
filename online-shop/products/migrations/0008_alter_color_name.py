# Generated by Django 4.0.2 on 2023-08-06 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_color_name_alter_color_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(default='white', max_length=300, null=True),
        ),
    ]
