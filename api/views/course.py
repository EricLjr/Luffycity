from django.shortcuts import render, HttpResponse
# from django.views import View
# from rest_framework.viewsets import ModelViewSet
from api.serializers import course
from api.utils.response import BaseResponse
from rest_framework.views import APIView
from api.models import CourseCategory, CourseSubCategory, \
    DegreeCourse, Teacher, Scholarship, Course, CourseDetail, OftenAskedQuestion, \
    CourseOutline, CourseChapter, CourseSection, CourseSection, CourseSection
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

# class Courses(ModelViewSet):
#     queryset=Course.objects.all()
#     serializer_class =app01_serializers.Course_serializers

class CourseView(APIView):
    # versioning_class=URLPathVersioning 指定我的version版本，
    # 其实就是告诉你去哪里能找到我的version信息，然后执行self.version_param, self.default_version再返回version
    # 默认可以在settings里设置
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:

            queryset = Course.objects.filter(degree_course__isnull=True)
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)
            serializer_class = course.CourseSerializers(instance=course_list, many=True)
            ret.data = serializer_class.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取失败，寸头再来'

        return Response(ret.dict)