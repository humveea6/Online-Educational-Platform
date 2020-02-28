import xadmin
from xadmin.layout import Fieldset, Main, Side, Row, FormHelper
from apps.courses.models import Course,Lesson,Video,CourseResource,BannerCourse
from import_export import resources

# class CourseAdmin(object):
#     list_display = ['name','desc','detail','degree','learn_time','students_num']
#     search_fields = ['name','desc','detail','degree','students_num']
#     list_filter = ['name','desc','detail','degree','learn_time','students_num']
#     list_editable = ['degree', 'desc']

#为广告课程添加单独的后台设置栏目
class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students_num']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students_num']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students_num']
    list_editable = ['degree', 'desc']

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs=qs.filter(is_banner=True)
        return qs

#在课程界面中同步编辑其他页面（课程章节，资源）
class LessonInline(object):
    model=Lesson
    extra=0

class CourseResourseInline(object):
    model=CourseResource
    extra=0
    style='tab'

#使用第三方导入导出插件
class MyResource(resources.ModelResource):
    class Meta:
        model=Course


class NewCourseAdmin(object):
    import_export_args = {'import_resource_class': MyResource, 'export_resource_class': MyResource}
    list_display = ['name', 'desc','show_image',  'go_to','degree', 'learn_time', 'students_num']
    search_fields = ['name', 'desc',  'degree', 'students_num']
    list_filter = ['name', 'desc', 'degree', 'learn_time', 'students_num']
    list_editable = ['degree', 'desc']
    readonly_fields=['click_nums','students_num','fav_num','add_time']
    inlines=[LessonInline,CourseResourseInline]

    #富文本编辑器配置
    style_fields={
        "detail":"ueditor",
    }

    #对于每个教师只返回相应课程
    def queryset(self):
        qs = super(NewCourseAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(teacher=self.request.user.teacher)


    #自定义显示布局
    def get_form_layout(self):
        self.form_layout = (
            Main(
                Fieldset("讲师信息",
                         'teacher','course_org',
                         css_class='unsort no_title'
                         ),
                Fieldset("基本信息",
                         'name','desc',
                         Row('learn_time','degree'),
                         Row('category','tag'),
                ),
                Fieldset('课程详情',
                         'you_need_know','teacher_says','notice','detail'

                ),
                Fieldset('广告信息',
                         'image','is_banner'
                ),
            ),
            Side(
                Fieldset(('访问信息'),
                         'students_num', 'fav_num', 'click_nums','add_time'
                         ),
            )
        )

        return super(NewCourseAdmin, self).get_form_layout()


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



# xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Course,NewCourseAdmin)

xadmin.site.register(BannerCourse,BannerCourseAdmin)

xadmin.site.register(Lesson,LessonAdmin)

xadmin.site.register(Video,VideoAdmin)

xadmin.site.register(CourseResource,CourseResourceAdmin)