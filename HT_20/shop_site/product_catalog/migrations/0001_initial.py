# Generated by Django 4.0.1 on 2022-02-06 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the product category', max_length=50, verbose_name='Product category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the product name', max_length=50, verbose_name='Product name')),
                ('description', models.TextField(help_text='Enter the product description', max_length=300, verbose_name='Product description')),
                ('category', models.ForeignKey(help_text='Enter category product', on_delete=django.db.models.deletion.CASCADE, to='product_catalog.category', verbose_name='Category product')),
            ],
        ),
    ]