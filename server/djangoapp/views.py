
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
import logging
import json
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            data = {
                "userName": username,
                "status": "Authenticated"
            }
        else:
            data = {
                "userName": username,
                "status": "Authentication failed"
            }

        return JsonResponse(data)

    return JsonResponse({"error": "POST request required"}, status=405)


@csrf_exempt
def logout_request(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({"userName": ""})

    return JsonResponse({"error": "POST request required"}, status=405)
