# Generated by Django 3.0.4 on 2020-06-01 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Server_app', '0012_auto_20200601_1524'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestTable',
        ),
    ]