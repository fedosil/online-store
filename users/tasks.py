from datetime import timedelta
from celery import shared_task
import uuid


from django.utils.timezone import now

from .models import Email_Verification, User


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = Email_Verification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verification_email()