from api.models import CourseCategory,CourseSubCategory,\
    DegreeCourse,Teacher,Scholarship,Course,CourseDetail,OftenAskedQuestion,\
    CourseOutline,CourseChapter,CourseSection,CourseSection,CourseSection
from rest_framework import serializers
#导入序列化模块
from rest_framework.validators import ValidationError
#导入模块中的错误类型
class CourseSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

