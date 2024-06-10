# Generated by Django 4.1 on 2023-01-12 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=100)),
                ('user_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municiplality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipality', models.CharField(max_length=200)),
                ('mayor', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='municipality')),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
