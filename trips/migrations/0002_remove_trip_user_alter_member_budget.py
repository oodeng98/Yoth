# Generated by Django 5.1 on 2024-08-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='user',
        ),
        migrations.AlterField(
            model_name='member',
            name='budget',
            field=models.IntegerField(default=0),
        ),
    ]
