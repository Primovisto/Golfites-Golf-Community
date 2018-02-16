# Generated by Django 2.0.1 on 2018-02-16 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0010_auto_20180201_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golferprofile',
            name='golfer',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
