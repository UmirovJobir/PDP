# Generated by Django 4.0.1 on 2022-01-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('imdb', models.IntegerField()),
                ('genre', models.CharField(max_length=300)),
            ],
        ),
    ]
