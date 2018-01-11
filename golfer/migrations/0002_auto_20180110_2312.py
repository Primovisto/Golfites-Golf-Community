# Generated by Django 2.0.1 on 2018-01-10 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='golferprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='golferprofile',
            name='swing',
            field=models.FileField(default='', upload_to='images'),
        ),
    ]