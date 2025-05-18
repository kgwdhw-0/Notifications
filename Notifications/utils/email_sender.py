from django.core.mail import send_mail

def send_email(notification):
    send_mail(
        subject=notification.subject or "No Subject",
        message=notification.message,
        from_email="no-reply@example.com",
        recipient_list=[f"{notification.user_id}"],  # simulate user email
        fail_silently=False
    )