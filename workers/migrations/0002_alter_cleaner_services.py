# Generated by Django 5.0.6 on 2024-06-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaner',
            name='services',
            field=models.ManyToManyField(to='workers.service'),
        ),
    ]
