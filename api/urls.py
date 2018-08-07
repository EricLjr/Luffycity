from django.conf.urls import url
from api.views import course,degree_course,\
    degree_course_scholarship,degree_model,\
    degree_course_recommend,question,CourseOutline,CourseChapter



urlpatterns = [
    # url(r'courses/',course.CourseView.as_view()),
    url(r'a/',degree_course.DegreeCourseView.as_view()),
    url(r'b/',degree_course_scholarship.DegreeCourseScholarship.as_view()),
    url(r'c/',course.CourseView.as_view()),
    url(r'd/',degree_model.CourseModelView.as_view()),
    url(r'e/',degree_course_recommend.DegreeCourseRecommendView.as_view()),
    url(r'f/',question.QuestionView.as_view()),
    url(r'g/',CourseOutline.CourseOutlineRecommendView.as_view()),
    url(r'h/',CourseChapter.CourseChapterView.as_view()),
]
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'courses', views.Courses)
# urlpatterns += router.urls