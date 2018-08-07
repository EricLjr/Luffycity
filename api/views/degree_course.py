
from api.utils.response import BaseResponse
from rest_framework.views import APIView
from api.models import DegreeCourse
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from api.serializers import degree_course


class DegreeCourseView(APIView):
    def get(self, request, *args, **kwargs):
        """
        查看所有学位课并打印学位课名称以及授课老师
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()
        try:
            queryset = DegreeCourse.objects.all()
            page = PageNumberPagination()
            degree_course_list = page.paginate_queryset(queryset, request, self)
            serializer_course = degree_course.DegreeCourseSerializer(instance=degree_course_list, many=True)
            ret.data = serializer_course.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取失败，葱头再来'
        return Response(ret.dict)
