# Generated by Django 4.2.6 on 2024-05-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_owner_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='capacity',
            field=models.IntegerField(default=None),
        ),
    ]