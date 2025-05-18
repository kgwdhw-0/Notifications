from django.db import models

class Notification(models.Model):
    NOTIF_TYPE_CHOICES = [
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
        ('IN_APP', 'In-App'),
    ]

    user_id = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=NOTIF_TYPE_CHOICES)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def _str_(self):
        return f"Notification({self.user_id}, {self.type}, {self.status})"