# Generated by Django 4.0.5 on 2022-06-15 07:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='modification date')),
                ('provider_name', models.CharField(max_length=50, unique=True, verbose_name='provider name')),
                ('email', models.EmailField(max_length=70, verbose_name='email')),
                ('phone_number', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='phone number')),
                ('language', models.CharField(choices=[('arabic', 'arabic'), ('english', 'english'), ('french', 'french'), ('spanish', 'spanish')], default='english', max_length=10, verbose_name='language')),
                ('currency', models.CharField(choices=[('DZD', 'DZD'), ('EUR', 'EUR'), ('USD', 'USD')], default='USD', max_length=3, verbose_name='Currency')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
