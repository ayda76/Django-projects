# Generated by Django 4.0.2 on 2023-09-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='qty',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
