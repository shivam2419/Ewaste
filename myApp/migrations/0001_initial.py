# Generated by Django 5.0.4 on 2024-11-17 15:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('message', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Index_gmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emails', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.EmailField(max_length=254)),
                ('pswrd', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QNA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=1000)),
                ('answers', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='RecycleForm',
            fields=[
                ('order_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_id', models.CharField(default=1, max_length=100, null=True)),
                ('organisation_id', models.CharField(default=1, max_length=100, null=True)),
                ('item_type', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='recycle_images/')),
                ('location', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(default=False, max_length=10, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='endUser',
            fields=[
                ('enduser_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('phone', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('organisation_id', models.AutoField(primary_key=True, serialize=False)),
                ('organisation_name', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('phone', models.IntegerField(null=True)),
                ('street', models.CharField(default='', max_length=400, null=True)),
                ('city', models.CharField(default='', max_length=400, null=True)),
                ('state', models.CharField(default='', max_length=400, null=True)),
                ('zipcode', models.CharField(default='', max_length=400, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
