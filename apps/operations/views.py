from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import messages

from apps.operations.models import UserFavourite,CourseComments,UserMessage
from apps.operations.forms import UserFavForm,CourseCommentForm
from apps.courses.models import Course
from apps.organizations.models import CourseOrg,Teacher


class CommentView(View):
    def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"用户未登录！")
            return JsonResponse({
                "status":"fail",
                "msg":"用户未登录"
            })

        course_comment_form=CourseCommentForm(request.POST)
        if course_comment_form.is_valid():
            course=course_comment_form.cleaned_data["course"]
            user_comment=course_comment_form.cleaned_data["comments"]

            comment=CourseComments()
            comment.user=request.user
            comment.comments=user_comment
            comment.course=course
            comment.save()

            return JsonResponse({
                "status":"success"
            })
        else:
            return JsonResponse({
                "status":"fail",
                "msg":"参数错误",
            })


class AddFavView(View):
    def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"用户未登录！")
            return JsonResponse({
                "status":"fail",
                "msg":"用户未登录"
            })

        user_fav_form=UserFavForm(request.POST)
        if user_fav_form.is_valid():
            fav_id=user_fav_form.cleaned_data["fav_id"]
            fav_type=user_fav_form.cleaned_data["fav_type"]

            existed_record=UserFavourite.objects.filter(user=request.user,fav_id=fav_id,fav_type=fav_type)
            if existed_record:
                existed_record.delete()

                if fav_type==1:
                    course=Course.objects.get(id=fav_id)
                    course.fav_num-=1
                    course.save()
                elif fav_type==2:
                    courseorg=CourseOrg.objects.get(id=fav_id)
                    courseorg.fav_nums-=1
                    courseorg.save()
                else:
                    teacher=Teacher.objects.get(id=fav_id)
                    teacher.fav_nums-=1
                    teacher.save()

                message = UserMessage()
                message.user = request.user
                message.messgae = "取消收藏成功！"
                message.has_read = False
                message.save()

                return JsonResponse({
                    "status":"success",
                    "msg":"收藏"
                })
            else:
                user_fav=UserFavourite()
                user_fav.fav_id=fav_id
                user_fav.fav_type=fav_type
                user_fav.user=request.user
                user_fav.save()

                if fav_type==1:
                    course=Course.objects.get(id=fav_id)
                    course.fav_num+=1
                    course.save()
                elif fav_type==2:
                    courseorg=CourseOrg.objects.get(id=fav_id)
                    courseorg.fav_nums+=1
                    courseorg.save()
                else:
                    teacher=Teacher.objects.get(id=fav_id)
                    teacher.fav_nums+=1
                    teacher.save()

                message = UserMessage()
                message.user = request.user
                message.messgae = "收藏成功！"
                message.has_read = False
                message.save()

                return JsonResponse({
                    "status":"success",
                    "msg":"已收藏"
                })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "参数错误"
            })








