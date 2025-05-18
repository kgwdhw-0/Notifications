from django.urls import path
from .views import NotificationCreateView, UserNotificationListView, in_app_notification_page

urlpatterns = [
    # API endpoints under /api/
    path('notifications/', NotificationCreateView.as_view(), name='send_notification'),
    path('users/<str:user_id>/notifications/', UserNotificationListView.as_view(), name='get_user_notifications'),

    # You can still keep in-app by user_id URL if needed
    path('in-app/<str:user_id>/', in_app_notification_page, name='in_app_page'),

    # (Optional) You can add '' here if you want notifications without prefix,
    # but better to do it in project urls.py for root '/'
]