# Generated by Django 3.2.11 on 2022-01-21 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='Users',
        ),
    ]