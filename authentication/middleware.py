# File: authentication/middleware.py

from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Update last_login_time if user is authenticated
        if request.user.is_authenticated:
            User.objects.filter(pk=request.user.pk).update(last_login_time=timezone.now())
        
        return response
