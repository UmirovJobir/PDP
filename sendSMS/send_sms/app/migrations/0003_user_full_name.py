# Generated by Django 4.0.3 on 2022-03-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default=1, max_length=20, verbose_name='имя абонента'),
            preserve_default=False,
        ),
    ]
