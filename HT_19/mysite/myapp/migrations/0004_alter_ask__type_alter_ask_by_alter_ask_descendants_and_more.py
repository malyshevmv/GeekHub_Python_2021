# Generated by Django 4.0.1 on 2022-02-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_job_url_alter_new_url_alter_show_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='_type',
            field=models.TextField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='ask',
            name='by',
            field=models.CharField(default=None, max_length=50, verbose_name='by'),
        ),
        migrations.AlterField(
            model_name='ask',
            name='descendants',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='ask',
            name='kids',
            field=models.TextField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='ask',
            name='score',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='ask',
            name='text',
            field=models.TextField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='ask',
            name='time',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='job',
            name='_type',
            field=models.TextField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='job',
            name='score',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='job',
            name='time',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='show',
            name='_type',
            field=models.TextField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='show',
            name='by',
            field=models.CharField(default=None, max_length=50, verbose_name='by'),
        ),
        migrations.AlterField(
            model_name='show',
            name='descendants',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='show',
            name='score',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='show',
            name='time',
            field=models.IntegerField(default=None),
        ),
    ]