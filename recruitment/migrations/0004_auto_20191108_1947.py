# Generated by Django 2.1 on 2019-11-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0003_auto_20191108_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='uid',
            field=models.IntegerField(default=0),
        ),
    ]
