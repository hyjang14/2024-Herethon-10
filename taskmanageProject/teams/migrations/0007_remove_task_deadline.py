# Generated by Django 5.0.6 on 2024-07-04 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
    ]