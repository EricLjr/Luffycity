from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'check/',views.Check.as_view())
]