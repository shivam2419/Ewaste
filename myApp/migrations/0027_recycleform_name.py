# Generated by Django 4.2.6 on 2024-05-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0026_alter_notification_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='recycleform',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]