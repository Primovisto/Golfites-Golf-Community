# Generated by Django 2.0.1 on 2018-01-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_ad_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='condition',
            field=models.CharField(default='Used', max_length=35),
        ),
    ]