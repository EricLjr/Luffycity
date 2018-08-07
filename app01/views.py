from django.shortcuts import render,HttpResponse
from django.views import View
import json
from api.models import CourseCategory,CourseSubCategory,\
    DegreeCourse,Teacher,Scholarship,Course,CourseDetail,OftenAskedQuestion,\
    CourseOutline,CourseChapter,CourseSection,CourseSection,CourseSection
# Create your views here.


class Check(View):
    def get(self,request):
        # a.查看所有学位课并打印学位课名称以及授课老师
        # c_obj=DegreeCourse.objects.all().values('name','teachers__name')
        # b.查看所有学位课并打印学位课名称以及学位课的奖学金
        # c_obj=DegreeCourse.objects.all()
        # for i in c_obj:
        #     print(i.name)
        #     print(i.degreecourse_price_policy.all().values('price'))
        # c. 展示所有的专题课
        # c_obj=Course.objects.filter(degree_course__isnull=True)
        # print(c_obj)
        #d. 查看id=1的学位课对应的所有模块名称
        # a_obj=DegreeCourse.objects.filter(id=1).values('course__name')
        # print(a_obj)
        #  e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
        # c_obj =Course.objects.filter(id=1)
        # print(c_obj.values('name'))
        # print(c_obj.first().get_level_display())
        # print(c_obj.values('coursedetail__why_study'))
        # print(c_obj.values('coursedetail__what_to_study_brief'))
        # print(c_obj.values('coursedetail__recommend_courses'))
        # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
        # c_obj = Course.objects.filter(id=1).first()
        # print(c_obj.asked_question.all().values('question'))
        # g.获取id = 1的专题课，并打印该课程相关的课程大纲
        # c_obj = Course.objects.filter(id=1)
        # print(c_obj.values('coursedetail__courseoutline__title'))

        # h.获取id = 1的专题课，并打印该课程相关的所有章节
        # c_obj = Course.objects.filter(id=1)
        # print(c_obj.values('coursechapters__name'))

        # i.获取id = 1的专题课，并打印该课程相关的所有课时
        # 第1章·Python 介绍、基础语法、流程控制
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 第1章·Python介绍、基础语法、流程控制
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # c_obj = Course.objects.filter(id=1)
        # for i in c_obj.values('coursechapters__chapter','coursechapters__name'):
        #     print(i.get('coursechapters__chapter'),i.get('coursechapters__name'))
        #     a_obj=CourseChapter.objects.filter(name=i.get('coursechapters__name'))
        #     for j in a_obj.values('coursesections__name'):
        #         print(j.get('coursesections__name'))

        # i.获取id = 1的专题课，并打印该课程相关的所有的价格策略
        # c_obj = Course.objects.filter(id=1).first()
        # print(c_obj.price_policy.all())

        return HttpResponse('ok')