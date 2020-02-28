import xadmin

from apps.organizations.models import Teacher,CourseOrg,City


class TeacherAdmin(object):
    list_display = ['name','org','work_year','work_company']
    search_fields = ['org','name','work_year','work_company']
    list_filter = ['org','name','work_year','work_company']


class TeacherInline(object):
    model=Teacher
    extra=0


class CourseOrgAdmin(object):
    list_display = [ 'name', 'click_nums','fav_nums']
    search_fields = ['name','click_nums','fav_nums']
    list_filter = ['name','click_nums','fav_nums']
    inlines=[TeacherInline]

    # 富文本编辑器配置
    style_fields = {
        "desc": "ueditor",
    }


class CityAdmin(object):
    list_display=['id','name','desc']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']
    list_editable=['name','desc']



xadmin.site.register(Teacher,TeacherAdmin)

xadmin.site.register(CourseOrg,CourseOrgAdmin)

xadmin.site.register(City,CityAdmin)