from api.serializers import degree_model
from api.utils.response import BaseResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import DegreeCourse

class CourseModelView(APIView):
    def get(self,request,*args,**kwargs):
        ret=BaseResponse()
        try:
            queryset=DegreeCourse.objects.get(id=1)
            serializer_lst=degree_model.DegreeModelSerializers(instance=queryset)
            ret.data=serializer_lst.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取失败，葱头再来'
        return Response(ret.dict)


