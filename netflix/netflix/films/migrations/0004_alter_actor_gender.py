# Generated by Django 4.0.1 on 2022-02-03 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(choices=[('Male', 'MAle'), ('Female', 'Female')], max_length=10),
        ),
    ]
