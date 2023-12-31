# Generated by Django 4.0.2 on 2023-11-13 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('onMenu', models.BooleanField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foods.cat')),
                ('ingredient', models.ManyToManyField(blank=True, null=True, to='foods.Ingredient')),
            ],
        ),
    ]
