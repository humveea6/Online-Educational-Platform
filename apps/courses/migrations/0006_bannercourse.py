# Generated by Django 2.2.10 on 2020-02-28 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_is_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '轮播课程',
                'verbose_name_plural': '轮播课程',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('courses.course',),
        ),
    ]
