from rest_framework  import  serializers
from api.models import Course
class DegreeCourseRecommendSerializers(serializers.ModelSerializer):
    level_name = serializers.CharField(source='get_level_display')
    why_studys = serializers.CharField(source='coursedetail.why_study')
    what_to_study_briefs = serializers.CharField(source='coursedetail.what_to_study_brief')

    recommend_courses = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id','name','level_name','why_studys','what_to_study_briefs','recommend_courses']

    def get_recommend_courses(self,row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [ {'id':item.id,'name':item.name} for item in recommend_list]