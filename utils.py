from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.core.Validators import validate_email

def send_email(recipient, subject, body):
    try:
        validate_email(recipient)
        send_email(
            subject,
            body,
            'from@example.com',
            [recipient],
            fail_silently=False,
        )
        return True
    except BadHeaderError:
        return False
    except ValidationError:
        return False