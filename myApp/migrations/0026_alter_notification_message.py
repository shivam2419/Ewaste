# Generated by Django 4.2.6 on 2024-05-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0025_notification_status_alter_notification_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]