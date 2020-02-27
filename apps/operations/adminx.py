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