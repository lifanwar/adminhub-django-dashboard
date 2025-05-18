from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
import requests

def group_list(request):
    return render(request, 'broadcast/group_list.html')

from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["POST"])
def fetch_groups(request):
    try:
        url = "https://chatbot.jastipin.id/group/fetchAllGroups/jastipin%20company"
        headers = {"apikey": "54B864DA9812-45D9-A5F0-73121DE9B145"}
        params = {"getParticipants": "false"}
        
        
        # Using requests.get directly with params for proper URL encoding
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=50,
            verify=False  # Skip SSL verification if needed
        )
        
        if response.status_code == 200:
            try:
                data = response.json()
                if isinstance(data, list):
                    # Transform data to only include id and subject fields
                    groups = []
                    for item in data:
                        if isinstance(item, dict) and "id" in item and "subject" in item:
                            groups.append({
                                "id": item["id"],
                                "name": item["subject"]  # Using 'subject' as the name field
                            })
                    
                    logger.info(f"Successfully processed {len(groups)} groups")
                    return JsonResponse({"groups": groups})
                else:
                    logger.error(f"Unexpected data format. Expected list, got: {type(data)}")
                    return JsonResponse({"error": "Invalid data format from server"}, status=500)
            except ValueError as e:
                logger.error(f"JSON parsing failed: {str(e)}")
                return JsonResponse({"error": "Invalid JSON response from server"}, status=500)
        else:
            logger.error(f"API returned non-200 status code: {response.status_code}")
            return JsonResponse(
                {"error": f"API request failed with status code: {response.status_code}"}, 
                status=response.status_code
            )
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return JsonResponse({"error": f"Failed to fetch groups: {str(e)}"}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

@require_http_methods(["POST"])
def save_groups(request):
    try:
        selected_groups = json.loads(request.body)
        # Here you would save the selected groups to your database
        return JsonResponse({
            "status": "success",
            "message": "Groups saved successfully"
        })
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=400)
