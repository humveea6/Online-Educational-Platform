import xadmin

from apps.operations.models import UserAsk,CourseComments,UserCourses,UserFavourite,UserMessage,Banner


#轮播图
class BannerAdmin(object):
    list_display = ['title','url','index']
    search_fields = ['title','url','index']
    list_filter = ['title','url','index']


class UserAskAdmin(object):
    list_display = ['name', 'mobile','course_name','add_time']
    search_fields = ['name', 'mobile','course_name']
    list_filter = ['name', 'mobile','course_name','add_time']


class UserCoursesAdmin(object):

    #新增数据时在别的表中进行同步
    def save_models(self):
        obj=self.new_obj
        if not obj.id:
            obj.save()
            course=obj.course
            course.students_num+=1
            course.save()

            #欢迎用户加入课程
            message = UserMessage()
            message.user = obj.user
            message.messgae = "欢迎您加入课程：{}的学习！".format(obj.course.name)
            message.has_read = False
            message.save()

        else:
            obj.save()

    pass


class UserFavouriteAdmin(object):
    pass


class CourseCommentAdmin(object):
    pass


class UserMessageAdmin(object):
    pass

xadmin.site.register(Banner,BannerAdmin)

xadmin.site.register(UserAsk,UserAskAdmin)

xadmin.site.register(UserCourses,UserCoursesAdmin)

xadmin.site.register(UserMessage,UserMessageAdmin)

xadmin.site.register(UserFavourite,UserFavouriteAdmin)

xadmin.site.register(CourseComments,CourseCommentAdmin)