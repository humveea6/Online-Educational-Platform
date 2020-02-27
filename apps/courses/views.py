from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from apps.courses.models import Course,CourseResource,Video
from apps.operations.models import UserFavourite,UserCourses,CourseComments

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


#课程视频播放
class VideoView(LoginRequiredMixin,View):
    login_url = "/login/"
    def get(self,request,course_id,video_id,*args,**kwargs):
        course=Course.objects.get(id=int(course_id))

        video=Video.objects.get(id=int(video_id))

        return render(request,"course-play.html",{
            "video":video,
            "course":course,
        })

#课程章节评论
class CourseCommentView(LoginRequiredMixin,View):
    login_url = "/login/"
    def get(self,request,course_id,*args,**kwargs):
        course=Course.objects.get(id=int(course_id))


        #课程评论
        course_comment=CourseComments.objects.filter(course=course)

        # 课程资源
        course_resource = CourseResource.objects.filter(course=course)


        # 学习过该课程的同学
        user_courses = UserCourses.objects.filter(course=course)
        user_ids = [user_course.user_id for user_course in user_courses]
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:3]
        related_couses = [user_course.course for user_course in all_courses]

        return render(request, "course-comment.html", {
            "course": course,
            "course_resource": course_resource,
            "all_courses": related_couses,
            "comments":course_comment,
        })

#课程章节信息
class CourseLessonView(LoginRequiredMixin,View):
    login_url = "/login/"
    def get(self,request,course_id,*args,**kwargs):
        course=Course.objects.get(id=int(course_id))

        #用户与课程的关系
        user_courses=UserCourses.objects.filter(user=request.user,course=course)
        if not user_courses:
            user_course=UserCourses(user=request.user,course=course)
            user_course.save()
            course.students_num+=1
            course.save()


        #课程资源
        course_resource=CourseResource.objects.filter(course=course)

        #学习过该课程的同学
        user_courses=UserCourses.objects.filter(course=course)
        user_ids=[user_course.user_id for user_course in user_courses]
        all_courses=UserCourses.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:3]
        related_couses=[user_course.course for user_course in all_courses]

        return render(request,"course-video.html",{
            "course":course,
            "course_resource":course_resource,
            "all_courses":related_couses,
        })


#课程详情页面
class CourseDetailView(View):
    def get(self,request,course_id,*args,**kwargs):
        course=Course.objects.get(id=int(course_id))
        course.click_nums+=1
        course.save()

        has_fav_course=False
        has_fav_org=False
        if request.user.is_authenticated:
            if UserFavourite.objects.filter(user=request.user,fav_id=course.id,fav_type=1):
                has_fav_course=True
            if UserFavourite.objects.filter(user=request.user,fav_id=course.course_org.id,fav_type=2):
                has_fav_org=True

        #课程推荐
        tag=course.tag
        related_course=[]
        if tag:
            related_course=Course.objects.filter(tag=tag)[:3]



        return render(request,"course-detail.html",{
            "course":course,
            "has_fav_course":has_fav_course,
            "has_fav_org":has_fav_org,
            "related_course":related_course,
        })


#课程列表页面
class CourseListView(View):
    def get(self,request,*args,**kwargs):
        all_courses=Course.objects.order_by("-add_time")
        hot_courses=Course.objects.order_by("-fav_num")[:3]

        #搜索关键字
        keywords=request.GET.get("keywords","")
        if keywords:
            all_courses=all_courses.filter(Q(name__icontains=keywords)|Q(desc__icontains=keywords)|Q(detail__icontains=keywords))

        #课程排序
        sort=request.GET.get("sort","")
        print(sort)
        if sort == "students":
            all_courses=all_courses.order_by("-students_num")
        elif sort=="hot":
            all_courses=all_courses.order_by("-click_nums")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_courses, per_page=3, request=request)

        courses = p.page(page)


        return render(request,"course-list.html",{
            "all_courses":courses,
            "sort":sort,
            "hot":hot_courses,
        })

