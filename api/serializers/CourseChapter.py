from rest_framework  import  serializers
from api.models import Course
class CourseChapterSerializers(serializers.ModelSerializer):
    course_chapter=serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['course_chapter']

    def get_course_chapter(self,obj):
        course_chapter_list = obj.coursechapters.all()
        return [ {'name':item.name} for item in course_chapter_list]