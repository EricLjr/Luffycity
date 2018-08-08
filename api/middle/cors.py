from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class Cors(MiddlewareMixin):
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin']='http://localhost:8080'
        if request.method=='OPTIONS':
            response["Access-Control-Allow-Methods"] = settings.CORS_METHODS
            response["Access-Control-Allow-Headers"] = settings.CORS_HEADERS
        return response