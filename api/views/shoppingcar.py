from api.serializers import priceserializers
from api.utils.response import BaseResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from api.models import CourseCategory, CourseSubCategory, \
    DegreeCourse, Teacher, Scholarship, Course, CourseDetail, OftenAskedQuestion, \
    CourseOutline, CourseChapter, CourseSection, CourseSection, CourseSection
from rest_framework.response import Response

ShoppingCar={'ljr':{}}
class ShoppingView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        pass
    def create(self,request,*args,**kwargs):
        """
        加入购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret=BaseResponse()
        course_name=request.data.get('course_name')
        price_id=request.data.get('price_period_id')
        course_obj=Course.objects.filter(name=course_name).first()
        if not course_obj:
            ret.code=500
            ret.error='把手从桌子底下拿出来，你从哪找的课？'
            return  Response(ret.dict)
        else:
            price_obj_list=course_obj.price_policy.all()
            for i in price_obj_list:
                print(price_id)
                if str(i.valid_period) == price_id:
                    print(11)
                    dic=ShoppingCar['ljr']

                    ser=priceserializers.PriceSerializers(price_obj_list,many=True)
                    dic[course_obj.pk]={'title':course_obj.name,'price_data':ser.data}
                    ret.data=ShoppingCar
                    return Response(ret.dict)
                else:
                    ret.code = 500
                    ret.error = '闯红灯是要罚款的？'
                    return Response(ret.dict)


        pass
    def retrieve(self,request,pk,*args,**kwargs):
        pass
    def update(self,request,pk,*args,**kwargs):
        pass
    def destroy(self,request,pk,*args,**kwargs):
        pass