import logging
import traceback
from django.http import JsonResponse
class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
      

        response = self.get_response(request)
      
        return response

    # view 裡發生錯誤會在這攔截 
    def process_exception(self, request, exception):
        logging.error(f"{  traceback.format_exc()}")
        return JsonResponse({'error': str(exception)}, status=500)