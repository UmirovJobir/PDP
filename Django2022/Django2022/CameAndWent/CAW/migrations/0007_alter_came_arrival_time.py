# Generated by Django 3.2.11 on 2022-01-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAW', '0006_alter_went_time_to_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='came',
            name='arrival_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]