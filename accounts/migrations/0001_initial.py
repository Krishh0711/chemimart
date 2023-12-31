# Generated by Django 4.2.3 on 2023-07-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('otp', models.CharField(max_length=6)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_buyer', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
