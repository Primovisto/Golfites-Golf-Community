# Generated by Django 2.0.1 on 2018-01-11 00:02

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0002_auto_20180110_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golferprofile',
            name='swing',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]