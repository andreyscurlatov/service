# Generated by Django 2.1 on 2019-11-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20191108_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='uid',
            field=models.IntegerField(),
        ),
    ]