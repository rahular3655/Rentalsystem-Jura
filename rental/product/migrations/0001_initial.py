# Generated by Django 4.1.7 on 2023-02-20 07:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('branch', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('Tag', models.CharField(max_length=50, null=True)),
                ('color', models.CharField(max_length=50, null=True)),
                ('size', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=15, null=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('is_available', models.BooleanField(default=True)),
                ('is_booked', models.BooleanField(default=False)),
                ('discount', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='photos/products')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categories')),
            ],
        ),
    ]