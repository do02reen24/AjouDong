# Generated by Django 3.0.4 on 2020-05-30 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Server_app', '0006_auto_20200525_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubstatistic',
            name='ITRatio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='Ratio13',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='Ratio14',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='Ratio15',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='Ratio16',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='Ratio17',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='Ratio18',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='Ratio19',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='engineeringRatio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='humanitiesRatio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='managementRatio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='naturalscienceRatio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='nurseRatio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='overRatio12',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clubstatistic',
            name='socialscienceRatio',
            field=models.IntegerField(),
        ),
    ]