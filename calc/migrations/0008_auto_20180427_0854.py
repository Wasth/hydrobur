# Generated by Django 2.0.4 on 2018-04-27 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='hekp',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='result',
            name='het',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='result',
            name='rekp',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='result',
            name='ret',
            field=models.CharField(max_length=100),
        ),
    ]