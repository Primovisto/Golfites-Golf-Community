# Generated by Django 2.0.1 on 2018-01-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education_center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('post_count', models.IntegerField(default=0)),
            ],
        ),
    ]
