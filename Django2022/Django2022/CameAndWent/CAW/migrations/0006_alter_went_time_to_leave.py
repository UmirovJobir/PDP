# Generated by Django 3.2.11 on 2022-01-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAW', '0005_auto_20220121_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='went',
            name='time_to_leave',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
