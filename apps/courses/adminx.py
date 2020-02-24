import xadmin

from apps.courses.models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_time','students_num']
    search_fields = ['name','desc','detail','degree','students_num']
    list_filter = ['name','desc','detail','degree','learn_time','students_num']
    list_editable = ['degree', 'desc']

class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['learn_time','name','add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']



class CourseResourceAdmin(object):
    list_display = ['course', 'name','file', 'add_time']
    search_fields = ['course', 'name','file']
    list_filter = ['course', 'name', 'file','add_time']



xadmin.site.register(Course,CourseAdmin)

xadmin.site.register(Lesson,LessonAdmin)

xadmin.site.register(Video,VideoAdmin)

xadmin.site.register(CourseResource,CourseResourceAdmin)