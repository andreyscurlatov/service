# Generated by Django 2.1 on 2019-12-03 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0008_auto_20191203_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='Электронный адрес почты'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.Planet', verbose_name='Планета'),
        ),
    ]