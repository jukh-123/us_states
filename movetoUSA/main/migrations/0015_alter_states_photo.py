# Generated by Django 4.2.7 on 2023-11-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_modelformap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='states',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Main photo'),
        ),
    ]