# Generated by Django 4.0.2 on 2023-08-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_postalcode_alter_profile_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]