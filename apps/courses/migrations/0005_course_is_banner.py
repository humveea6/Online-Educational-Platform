# Generated by Django 2.2.10 on 2020-02-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200225_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='是否在广告位展示'),
        ),
    ]
