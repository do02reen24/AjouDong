# Generated by Django 3.0.4 on 2020-05-31 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Server_app', '0008_auto_20200531_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('clubID', models.IntegerField(primary_key=True, serialize=False)),
                ('clubName', models.CharField(max_length=32)),
                ('clubCategory', models.CharField(max_length=256)),
                ('clubIMG', models.CharField(max_length=128)),
                ('clubMajor', models.IntegerField(default=1)),
                ('clubDues', models.FloatField(max_length=3)),
            ],
        ),
        
    ]
