# Generated by Django 4.2.7 on 2023-11-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='states',
            name='jobs',
            field=models.CharField(default='jobs title', max_length=255, verbose_name='State main jobs'),
        ),
        migrations.AddField(
            model_name='states',
            name='salary',
            field=models.IntegerField(default=1000, verbose_name='State average salary'),
        ),
    ]
