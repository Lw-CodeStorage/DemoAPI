from django.http import JsonResponse

class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
      

      
        response = self.get_response(request)
      
        return response

    def process_exception(self, request, exception):
    
        return JsonResponse({'error': 'Exception 處理的 Server Error'}, status=500)