from rest_framework  import  serializers
from api.models import DegreeCourse
class DegreeModelSerializers(serializers.ModelSerializer):
    model_list=serializers.SerializerMethodField()
    def get_model_list(self,obj):
        model_list=obj.course_set.all()
        print(model_list)
        return [{'name':i.name} for i in model_list]

    class Meta:
        model=DegreeCourse
        fields=['model_list']
