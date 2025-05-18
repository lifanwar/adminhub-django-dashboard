import json
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

def get_qr_code(request):
    url = "https://chatbot.jastipin.id/instance/connect/gurindamlian"
    querystring = {"number": "201501094150"}
    headers = {"apikey": "8832A7D1C700-4DE4-AGY0CD-96E481A95DF1"}
    
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        return JsonResponse(response.json())
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def disconnect(request):
    url = "https://chatbot.jastipin.id/instance/logout/gurindamlian"
    headers = {"apikey": "8832A7D1C700-4DE4-AGY0CD-96E481A95DF1"}
    
    try:
        response = requests.request("DELETE", url, headers=headers)
        return JsonResponse(response.json())
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def index(request):
    return render(request, 'dashboard/index.html')
