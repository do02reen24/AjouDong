# Generated by Django 3.0.4 on 2020-05-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Server_app', '0005_auto_20200525_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubactivity',
            name='clubActivityThumbnail',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
