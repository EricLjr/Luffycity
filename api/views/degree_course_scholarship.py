from rest_framework.views import APIView
# 继承rest里已经继承了django的View
from rest_framework.response import Response
# 响应器
from api.serializers import degree_course_scholarship
# 序列化
from rest_framework.pagination import PageNumberPagination
# 分页器
from api.utils.response import BaseResponse
# 通用字典
from api.models import DegreeCourse


# 表格
class DegreeCourseScholarship(APIView):
    def get(self, request, *args, **kwargs):
        """
         b.查看所有学位课并打印学位课名称以及学位课的奖学金
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()
        try:
            queryset = DegreeCourse.objects.all()
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)
            serializer_course = degree_course_scholarship.DegreeCourseScholarshipSerializers(instance=course_list,
                                                                                             many=True)
            ret.data = serializer_course.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取失败，葱头再来'
        return Response(ret.dict)
