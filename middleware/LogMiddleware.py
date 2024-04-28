import logging
import json
from django.http import JsonResponse

# 使用 'django.request' logger
logger = logging.getLogger('django.request')

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        # 記錄基本資訊
        logger.info(f'--------------------------------------------------------------------------------')
        logger.info(f'[Request]: {request.method} {request.path}')
        
        # 記錄 headers
        logger.info(f'Headers: {request.headers}')

         # 記錄 POST 資料
        if request.method == 'POST':
            logger.info(f'POST Data: {json.loads(request.body)}')

        # 記錄 GET 參數
        if request.method == 'GET':
            get_params = request.GET.dict()
            logger.info(f'GET Params: {get_params}')


        # 調用 get_response 方法並獲取 response
        response = self.get_response(request)
        
        # 記錄 response
        logging.info(f"[Response] {response.content}")
        
        return response
    
