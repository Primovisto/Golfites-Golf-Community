# Generated by Django 2.0.1 on 2018-01-26 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0004_auto_20180125_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golferprofile',
            name='golfer',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]