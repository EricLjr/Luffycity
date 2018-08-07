from api.serializers import question
from api.utils.response import BaseResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Course

class QuestionView(APIView):
    def get(self,request,*args,**kwargs):
        ret=BaseResponse()
        try:
            queryset=Course.objects.get(id=1)
            serializer_lst=question.QuestionSerializers(instance=queryset)
            ret.data=serializer_lst.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取失败，葱头再来'
        return Response(ret.dict)
