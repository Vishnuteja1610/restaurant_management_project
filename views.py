from django.http import JsonResponse
from utils.validation_utils import is_valid_email

def validate_user_email(request):
    email = request.GET.get("email","")
    if is_valid_email(email):
        return JsonResponse({"vaild":True, "message":"Valid email"})
    else:
        return JsonResponse({"valid":False, "message": "Invalid email"})
        