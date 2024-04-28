
from django.http import JsonResponse
class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        # return JsonResponse({'data':'身分授權未通過'},status = 401)

        # 調用 get_response 方法並獲取 response
        response = self.get_response(request)
        
        return response
    
