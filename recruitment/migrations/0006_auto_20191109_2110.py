# Generated by Django 2.1 on 2019-11-09 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0005_handshadow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handshadow',
            name='recruit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hands', to='recruitment.Recruit'),
        ),
    ]