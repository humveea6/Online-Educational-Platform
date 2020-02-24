from django.shortcuts import render
from django.views.generic.base import View


from apps.organizations.models import CourseOrg,City


from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# from mxonline.settings import MEDIA_URL

class OrgView(View):
    def get(self,request,*args,**kwargs):
        all_orgs=CourseOrg.objects.all()
        # org_nums=CourseOrg.objects.count()
        city_list=City.objects.all()
        

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
        })
