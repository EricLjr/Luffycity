from rest_framework  import  serializers
from api.models import Course
class CourseOutlineSerializers(serializers.ModelSerializer):
    course_outline=serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['course_outline']

    def get_course_outline(self,obj):
        course_outline = obj.coursedetail.courseoutline_set.all()
        return [ {'title':item.title,'content':item.content} for item in course_outline]