# Generated by Django 2.2.10 on 2020-02-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20200223_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='org/%Y/%m', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='name',
            field=models.CharField(max_length=50, verbose_name='机构名称'),
        ),
    ]
