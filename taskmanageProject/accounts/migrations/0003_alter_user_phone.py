# Generated by Django 5.0.6 on 2024-07-01 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=30, unique=True, verbose_name='전화번호'),
        ),
    ]
