from rest_framework import serializers

from notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['resource', 'user_id', 'topic', 'application_id', 'attempts', 'sent', 'received']

    def create(self, validated_data):
        
        return Notification.objects.create(**validated_data)
        