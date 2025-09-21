from django.core.mail import send_mail
from django.conf import settings
import logging

def send_order_confirmation_email(order_id, customer_email, customer_name, order_details):
    subject = f"Order confirmation - Order #{order_id}"
    message = (
        f"Dear{customer_name},\n\n"
        f"Thank you for your order!\n"
        f"Order ID:{order_id}\n "
        f"Order Details:{order_details}\n\n "
        "We appreciate your business!"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]
    try:
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
        return True
    except Exception as e:
        logging.error(f"Order confirmation email failed for order {order_id}: {e}")
        return False