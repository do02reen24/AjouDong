# Generated by Django 3.0.4 on 2020-06-02 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Server_app', '0014_auto_20200602_1516'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='appliedclublist',
            name='applyDate',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
