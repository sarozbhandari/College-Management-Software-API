# Generated by Django 2.2 on 2019-08-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20190812_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmanagement',
            name='university_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
