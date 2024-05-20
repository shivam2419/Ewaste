# Generated by Django 4.2.6 on 2024-05-05 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_index_gmails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=200)),
                ('longitude', models.FloatField()),
                ('latitue', models.FloatField()),
                ('phone', models.IntegerField(max_length=1000)),
            ],
        ),
    ]