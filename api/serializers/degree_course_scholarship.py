from rest_framework  import  serializers
from api.models import DegreeCourse
class DegreeCourseScholarshipSerializers(serializers.ModelSerializer):
    scholarship_list=serializers.SerializerMethodField()
    def get_scholarship_list(self,obj):
        scholarship_list=obj.scholarship_set.all()
        return [{'value':i.value,'percent':i.time_percent} for i in scholarship_list]

    class Meta:
        model=DegreeCourse
        fields=['name','scholarship_list']