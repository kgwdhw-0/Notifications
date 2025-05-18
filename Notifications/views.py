from rest_framework import generics
from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer
from .utils.email_sender import send_email
from .utils.sms_sender import send_sms
from .utils.in_app_handler import save_in_app_notification


def in_app_notification_page(request, user_id):
    notifications = Notification.objects.filter(user_id=user_id, type='IN_APP').order_by('-created_at')
    return render(request, 'notifications/in_app.html', {'notifications': notifications, 'user_id': user_id})


class NotificationCreateView(generics.CreateAPIView):
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        notification = serializer.save()
        if notification.type == 'EMAIL':
            send_email(notification)
        elif notification.type == 'SMS':
            send_sms(notification.phone_number, notification.message)
        elif notification.type == 'IN_APP':
            save_in_app_notification(notification)
        notification.status = 'SENT'
        notification.save()


class UserNotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Notification.objects.filter(user_id=user_id).order_by('-created_at')