# Generated by Django 5.1.2 on 2024-10-19 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_staffavailability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='day',
        ),
    ]
