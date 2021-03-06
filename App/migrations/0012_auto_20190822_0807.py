# Generated by Django 2.2 on 2019-08-22 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20190818_0801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sessionmanagement',
            options={'ordering': ('-start_date',)},
        ),
        migrations.AddField(
            model_name='grademanagement',
            name='internal_marks',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='grademanagement',
            name='total_marks',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 8, 22)),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='start_date',
            field=models.DateField(default=datetime.date(2019, 8, 22)),
        ),
        migrations.AlterField(
            model_name='grademanagement',
            name='grades',
            field=models.CharField(max_length=299),
        ),
        migrations.AlterField(
            model_name='grademanagement',
            name='marks',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='grademanagement',
            name='status',
            field=models.CharField(max_length=288),
        ),
        migrations.AlterField(
            model_name='sessionmanagement',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 8, 22)),
        ),
        migrations.AlterField(
            model_name='sessionmanagement',
            name='start_date',
            field=models.DateField(default=datetime.date(2019, 8, 22)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='date_created',
            field=models.DateField(default=datetime.date(2019, 8, 22)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='enrolled_year',
            field=models.DateField(default=datetime.date(2019, 8, 22)),
        ),
    ]
