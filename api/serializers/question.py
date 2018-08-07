from rest_framework  import  serializers
from api.models import Course
class QuestionSerializers(serializers.ModelSerializer):
    questions=serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['questions']

    def get_questions(self,obj):
        question_list = obj.asked_question.all()
        return [ {'question':item.question,'answer':item.answer} for item in question_list]