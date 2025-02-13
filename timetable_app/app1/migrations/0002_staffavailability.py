# Generated by Django 5.1.2 on 2024-10-19 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.day')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.staff')),
            ],
        ),
    ]
