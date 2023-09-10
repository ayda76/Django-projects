# Generated by Django 4.0.2 on 2023-09-10 15:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='ing',
            field=models.ManyToManyField(blank=True, null=True, to='foods.Ingredient'),
        ),
    ]