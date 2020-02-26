from django.db import models
from apps.users.models import BaseModel
from apps.organizations.models import Teacher,CourseOrg
# Create your models here.

class Course(BaseModel):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name="课程老师")
    course_org=models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name="课程机构",null=True,blank=True)
    name=models.CharField(verbose_name="课程名",max_length=50)
    desc=models.CharField(verbose_name="课程描述",max_length=300)
    learn_time=models.IntegerField(default=0,verbose_name="学习时长（分钟数）")
    degree=models.CharField(verbose_name="难度",choices=(("junior","初级"),("middle","中级"),("senior","高级")),max_length=6)
    students_num=models.IntegerField(default=0,verbose_name="学习人数")
    fav_num=models.IntegerField(default=0,verbose_name="收藏人数")
    click_nums=models.IntegerField(default=0,verbose_name="点击数")
    category=models.CharField(default="后端开发",max_length=20,verbose_name="课程类型")
    tag=models.CharField(default="",verbose_name="课程标签",max_length=10)
    you_need_know=models.CharField(default="",max_length=300,verbose_name="课程须知")
    teacher_says=models.CharField(default="",max_length=300,verbose_name="老师告诉你")
    notice=models.CharField(verbose_name="课程公告",max_length=200,default="")

    detail=models.TextField(verbose_name="课程详情")
    image=models.ImageField(upload_to="course/%Y/%m",verbose_name="封面图",max_length=100,blank=True,null=True)

    class Meta:
        verbose_name="课程信息"
        verbose_name_plural=verbose_name


    def __str__(self):
        return self.name

    def lesson_nums(self):
        return self.lesson_set.all().count()



class Lesson(BaseModel):
    course =models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name="章节名")
    learn_time=models.IntegerField(default=0,verbose_name="学习时长（分钟数）")


    class Meta:
        verbose_name="课程章节"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Video(BaseModel):
    lesson=models.ForeignKey(Lesson,verbose_name="章节",on_delete=models.CASCADE)
    name=models.CharField(max_length=100,verbose_name="视频名")
    learn_time=models.IntegerField(default=0,verbose_name="学习时长（分钟数）")
    url=models.CharField(max_length=1000,verbose_name="访问地址")

    class Meta:
        verbose_name=  "视频"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class CourseResource(BaseModel):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="课程")
    name=models.CharField(max_length=100,verbose_name="名称")
    file=models.FileField(upload_to="course/resource/%Y/%m",verbose_name="下载地址",max_length=200)

    class Meta:
        verbose_name=  "课程资源"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name