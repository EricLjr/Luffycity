from rest_framework import serializers
from api.models import DegreeCourse


class DegreeCourseSerializer(serializers.ModelSerializer):
    teachers_list = serializers.SerializerMethodField()

    def get_teachers_list(self, obj):
        teachers_list = obj.teachers.all()
        return [{'name': i.name} for i in teachers_list]

    class Meta:
        model = DegreeCourse
        fields = ['name', 'teachers_list']
