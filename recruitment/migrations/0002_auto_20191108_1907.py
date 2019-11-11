# Generated by Django 2.1 on 2019-11-08 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='recruit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recruitment.Recruit'),
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recruitment.Question'),
        ),
        migrations.AlterField(
            model_name='planet',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sith',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]