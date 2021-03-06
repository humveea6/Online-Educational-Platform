from django.db import models

from apps.users.models import BaseModel
from apps.courses.models import Course

from django.contrib.auth import get_user_model


UserProfile=get_user_model()


#首页轮播图
class Banner(BaseModel):
    title=models.CharField(max_length=100,verbose_name="标题")
    image=models.ImageField(upload_to="banner/%Y/%m",max_length=200,verbose_name="轮播图")
    url=models.URLField(max_length=300,verbose_name="访问地址",null=True,blank=True)
    index=models.IntegerField(default=0,verbose_name="展示优先级（越小越高）")

    class Meta:
        verbose_name="轮播图"
        verbose_name_plural=verbose_name


    def __str__(self):
        return self.title


class UserAsk(BaseModel):
    name =models.CharField(max_length=20,verbose_name="姓名")
    mobile=models.CharField(max_length=11,verbose_name="手机号码")
    course_name=models.CharField(max_length=50,verbose_name="课程名")

    class Meta:
        verbose_name="用户咨询"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{name}_{course}({mobile})".format(name=self.name,course=self.course_name,mobile=self.mobile)


class CourseComments(BaseModel):
    user=models.ForeignKey(UserProfile,verbose_name="用户",on_delete=models.CASCADE)
    course=models.ForeignKey(Course,verbose_name="课程",on_delete=models.CASCADE)
    comments=models.CharField(max_length=200,verbose_name="评论内容")

    class Meta:
        verbose_name="课程评论"
        verbose_name_plural=verbose_name


    def __str__(self):
        return self.comments



class UserFavourite(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    fav_id = models.IntegerField( verbose_name="课程")
    fav_type=models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"讲师")),default=1,verbose_name="收藏类型")

    class Meta:
        verbose_name="用户收藏"
        verbose_name_plural=verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user,id=self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    #course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    messgae = models.CharField(max_length=200, verbose_name="消息内容")
    has_read=models.BooleanField(default=False,verbose_name="是否已读")
    # add_time = models.

    class Meta:
        verbose_name="用户消息"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.messgae


class UserCourses(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)

    class Meta:
        verbose_name="用户课程"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.course.name