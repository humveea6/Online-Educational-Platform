from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
from apps.users.models import BaseModel,UserProfile

class City(BaseModel):
    name=models.CharField(max_length=50,verbose_name="城市")
    desc=models.CharField(max_length=200,verbose_name="描述")

    class Meta:
        verbose_name="城市列表"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name



class CourseOrg(BaseModel):
    city=models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="所在城市")
    name=models.CharField(max_length=50,verbose_name="机构名称")
    desc=UEditorField(verbose_name="描述",width=900,height=400,imagePath="organizations/ueditor/images/",
                        filePath="organizations/ueditor/files/",default="")
    tag=models.CharField(default="全国知名",max_length=10,verbose_name="机构标签")
    category=models.CharField(default="pxjg",verbose_name="机构类别",max_length=4,
                              choices=(("pxjg","培训机构"),("gr","个人"),("gx","高校")))
    click_nums=models.IntegerField(verbose_name="点击数量",default=0)
    fav_nums=models.IntegerField(default=0,verbose_name="收藏数")
    image=models.ImageField(upload_to="org/%Y/%m",verbose_name="logo",max_length=100,null=True,blank=True)
    address=models.CharField(max_length=150,verbose_name="机构地址")
    stu_num=models.IntegerField(default=0,verbose_name="学习人数")
    course_num=models.IntegerField(default=0,verbose_name="课程数")

    is_auth=models.BooleanField(default=False,verbose_name="是否认证")
    is_gold=models.BooleanField(default=False,verbose_name="是否推荐")

    class Meta:
        verbose_name="课程机构"
        verbose_name_plural=verbose_name


    def __str__(self):
        return self.name

    def courses(self):
        # from apps.courses.models import Course
        # course =Course.objects.filter(course_org=self)
        course=self.course_set.all()[:3]
        return course

    def teacher_num(self):
        return self.teacher_set.all().count()

    # 自定义后台列显示方法
    def show_image(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<img src='{}'>".format(self.image.url))

    show_image.short_description = "机构封面图"


class Teacher(BaseModel):
    user=models.OneToOneField(UserProfile,null=True,blank=True,on_delete=models.CASCADE,verbose_name="对应系统用户名 ")
    name=models.CharField(max_length=50,verbose_name="教师名")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    work_year=models.IntegerField(default=0,verbose_name="工作年限")
    work_company=models.CharField(max_length=50,verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(verbose_name="点击数量", default=0)
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    age = models.IntegerField(default=0, verbose_name="年龄")
    image=models.ImageField(upload_to="teacher/%Y/%m",verbose_name="头像",max_length=100,null=True,blank=True)
    is_gold = models.BooleanField(default=False, verbose_name="是否推荐")

    class Meta:
        verbose_name="教师"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        return self.course_set.all().count()



