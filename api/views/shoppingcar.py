import json
import redis

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework.parsers import JSONParser, FormParser

from api.models import Course
from api.serializers import priceserializers
from api.utils.response import BaseResponse

CONN = redis.Redis(host='192.168.11.157', port=6379)

USER_ID = '1'


class ShoppingView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 10000, 'data': None, 'error': None}
        try:
            shopping_car_course_list = []

            # pattern = "shopping_car_%s_*" % (USER_ID,)
            pattern = settings.LUFFY_SHOPPING_CAR % (USER_ID, '*',)

            user_key_list = CONN.keys(pattern)
            for key in user_key_list:
                temp = {
                    'id': CONN.hget(key, 'id').decode('utf-8'),
                    'name': CONN.hget(key, 'name').decode('utf-8'),
                    'img': CONN.hget(key, 'img').decode('utf-8'),
                    'default_price_id': CONN.hget(key, 'default_price_id').decode('utf-8'),
                    'price_policy_dict': json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
                }
                shopping_car_course_list.append(temp)

            ret['data'] = shopping_car_course_list
        except Exception as e:
            ret['code'] = 10005
            ret['error'] = '获取购物车数据失败'

        return Response(ret)

    def create(self, request, *args, **kwargs):
        """
        加入购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = BaseResponse()
        # 1.接受用户选中的课程ID和价格策略ID
        course_id = request.data.get('course_id')
        policy_id = request.data.get('policy_id')
        # 2. 判断合法性
        #   - 课程是否存在？
        #   - 价格策略是否合法？

        # 2.1 课程是否存在？
        course_obj = Course.objects.filter(id=course_id).first()
        if not course_obj:
            ret.code = 500
            ret.error = '课程不存在，把手拿上来'
            return Response(ret.dict)
        # 2.2 价格策略是否合法？
        price_policy_list = course_obj.price_policy.all()
        price_policy_dict = {}
        for item in price_policy_list:
            temp = {
                'id': item.id,
                'price': item.price,
                'valid_period': item.valid_period,
                'valid_period_display': item.get_valid_period_display()
            }
            price_policy_dict[item.id] = temp
        #     {1: {'price': 666666.0, 'valid_period': 180, 'id': 1, 'valid_period_display': '6个月'}, 5: {'price': 6472346.0, 'valid_period': 540, 'id': 5, 'valid_period_display': '18个月'}}
        if policy_id not in price_policy_dict:
            ret.code = 500
            ret.error = '价格策略不存在，把手拿上来'
            return Response(ret.dict)
        # 3. 把商品和价格策略信息放入购物车 SHOPPING_CAR
        # 3.1如果购物车中的商品数量超过了限定，需要限制用户加入
        pattern = 'shopping_car_%s_%s' % (USER_ID, '*')
        keys = CONN.keys(pattern)
        if keys and len(keys) >= 100:
            ret.code = 500
            ret.error = '东西太多了，先结账把'
            return Response(ret.dict)
        hash = 'shopping_car_%s_%s' % (USER_ID, course_id)
        # 批量生成hash内部的键值对
        CONN.hmset(hash, {
            'id': course_id,
            'name': course_obj.name,
            'img': course_obj.course_img,
            'default_price_id': policy_id,
            'price_policy_dict': json.dumps(price_policy_dict)
        })
        # 设置hash数据存在时间

        CONN.expire(hash, 20 * 60)
        return Response({'code': 10000, 'data': '购买成功'})

    def retrieve(self, request, pk, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        """
        修改用户选中的价格策略
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        """
        1. 获取课程ID、要修改的价格策略ID
        2. 校验合法性（去redis中）
        """
        response = BaseResponse()
        try:
            course_id = request.data.get('course_id')
            policy_id = str(request.data.get('policy_id')) if request.data.get('policy_id') else None

            # key = 'shopping_car_%s_%s' %(USER_ID,course_id,)
            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, course_id,)

            if not CONN.exists(key):
                #如果Redis中不存在这个key的hash,则为不合法
                response.code = 1001
                response.error = '课程不存在'
                return Response(response.dict)

            price_policy_dict = json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
            if policy_id not in price_policy_dict:
                response.code = 1002
                response.error = '价格策略不存在'
                return Response(response.dict)

            CONN.hset(key, 'default_price_id', policy_id)
            CONN.expire(key, 20 * 60)
            response.data = '修改成功'
        except Exception as e:
            response.code = 1003
            response.error = '修改失败'

        return Response(response.dict)

    def destroy(self, request, *args, **kwargs):
        """
        删除购物车中的某个课程
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = BaseResponse()
        try:
            #首先得到一个课程id
            course_id = request.GET.get('course_id')
            # key = "shopping_car_%s_%s" % (USER_ID,courseid)
            key = settings.LUFFY_SHOPPING_CAR % (USER_ID, course_id,)

            CONN.delete(key)
            # 在Redis中将带有这个课程id的hash删除
            response.data = '删除成功'
        except Exception as e:
            response.code = 10006
            response.error = '删除失败'
        return Response(response.dict)
