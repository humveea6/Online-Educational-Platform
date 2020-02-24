from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile
import xadmin

# class UserProfileAdmin(admin.ModelAdmin):
#     pass


class GlobalSettings(object):
    site_title="慕学后台管理系统"
    site_footer="慕学在线网"


class BaseSettings(object):
    enable_themes=True
    use_bootswatch=True

xadmin.site.register(xadmin.views.CommAdminView,GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView,BaseSettings)
#admin.site.register(UserProfile,UserAdmin)


