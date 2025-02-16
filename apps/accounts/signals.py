# accounts/signals.py
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import LoginLog

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip_address = request.META.get('REMOTE_ADDR')
    LoginLog.objects.create(user=user, ip_address=ip_address)
