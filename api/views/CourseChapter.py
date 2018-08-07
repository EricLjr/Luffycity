from api.serializers import CourseChapter
from api.utils.response import BaseResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Course

class CourseChapterView(APIView):
    def get(self,request,*args,**kwargs):
        ret=BaseResponse()
        try:
            queryset=Course.objects.get(id=1)
            serializer_lst=CourseChapter.CourseChapterSerializers(instance=queryset)
            ret.data=serializer_lst.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取失败，葱头再来'
        return Response(ret.dict)
