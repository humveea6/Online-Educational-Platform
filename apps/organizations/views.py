from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse


from apps.organizations.models import CourseOrg,City
from apps.organizations.forms import AddAskForm
from apps.operations.models import UserFavourite


from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# from mxonline.settings import MEDIA_URL


#机构主页
class OrgHomeView(View):
    def get(self,request,org_id,*args,**kwargs):
        course_org=CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums +=1
        course_org.save()

        has_fav=False
        if request.user.is_authenticated:
            if UserFavourite.objects.filter(user=request.user,fav_id=course_org.id,fav_type=2):
                has_fav=True



        all_courses=course_org.course_set.all()[0:3]
        all_teachers=course_org.teacher_set.all()[:1]

        current_page = "home"

        return render(request,"org-detail-homepage.html",{
            "all_courses":all_courses,
            "all_teachers":all_teachers,
            "course_org":course_org,
            "current_page":current_page,
            "has_fav":has_fav,
        })


#机构教师
class OrgTeacherView(View):
    def get(self,request,org_id,*args,**kwargs):
        course_org=CourseOrg.objects.get(id=int(org_id))
        all_teachers=course_org.teacher_set.all()
        current_page="teacher"
        has_fav = False
        if request.user.is_authenticated:
            if UserFavourite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request, "org-detail-teachers.html", {
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page":current_page,
            "has_fav": has_fav,
        })

#机构课程
class OrgCourseView(View):
    def get(self,request,org_id,*args,**kwargs):
        course_org=CourseOrg.objects.get(id=int(org_id))
        all_courses=course_org.course_set.all()
        current_page="course"

        has_fav = False
        if request.user.is_authenticated:
            if UserFavourite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        # 第三方分页库  https://github.com/jamespacileo/django-pure-pagination
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_courses, per_page=5, request=request)

        courses = p.page(page)

        return render(request, "org-detail-course.html", {
            "all_courses": courses,
            "course_org": course_org,
            "current_page":current_page,
            "has_fav": has_fav,
        })


#机构介绍
class OrgDescView(View):
    def get(self,request,org_id,*args,**kwargs):
        course_org=CourseOrg.objects.get(id=int(org_id))
        current_page="desc"

        has_fav = False
        if request.user.is_authenticated:
            if UserFavourite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request, "org-detail-desc.html", {
            "course_org": course_org,
            "current_page":current_page,
            "has_fav": has_fav,
        })


#用户咨询
class AddAskView(View):
    def post(self,request,*args,**kwargs):
        userask_form=AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status":"success"
            })
        else:
            return JsonResponse({
                "status":"fail",
                "msg":"提交信息出错！"
            })


#机构列表页面
class OrgView(View):
    def get(self,request,*args,**kwargs):
        all_orgs=CourseOrg.objects.all()
        # org_nums=CourseOrg.objects.count()
        city_list=City.objects.all()

        #机构热度排序
        hot_orgs=all_orgs.order_by("-click_nums")[:3]


        #通过机构类别对课程机构进行筛选
        category=request.GET.get("ct","")
        if category:
            all_orgs=all_orgs.filter(category=category)


        #通过城市进行筛选
        city_id=request.GET.get("city","")
        if city_id:
            if city_id.isdigit():
                all_orgs=all_orgs.filter(city_id=int(city_id))

        org_nums = all_orgs.count()

        #对机构进行排序
        sort=request.GET.get("sort","")
        if sort == "students":
            all_orgs=all_orgs.order_by("-stu_num")
        elif sort =="courses":
            all_orgs=all_orgs.order_by("-course_num")


        #第三方分页库  https://github.com/jamespacileo/django-pure-pagination
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1


        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs,per_page=5,request=request)

        orgs = p.page(page)

        return render(request,"org-list.html",{
            "all_orgs":orgs,
            # "MEDIA_URL":MEDIA_URL,
            "org_nums":org_nums,
            "city_list":city_list,
            "category":category,
            "city_id":city_id,
            "sort":sort,
            "hot_orgs":hot_orgs,
        })
