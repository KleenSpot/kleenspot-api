from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from .models.models import CustomUser, LoginHistory


@receiver(user_logged_in, sender=CustomUser)
def user_logged_in_receiver(request, user, **kwargs):
    #save last login time
    user.last_login_time = timezone.now()
    user.save()
    LoginHistory.objects.create(user=user, ip_address=request.META['REMOTE_ADDR'])

@receiver(user_logged_out, sender=CustomUser)
def user_logged_out_receiver( user, **kwargs):
    user.last_logout_time = timezone.now()
    user.save()
    # get how long a user has been inactive
    if user.last_login_time:
       user.inactive_duration = timezone.now() - user.last_login_time
    user.save()

