from rest_framework import serializers
from .models import WeeklyLog

class WeeklyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyLog
        fields = '__all__'
        read_only_fields = ['status', 'student']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['student'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # ❗ Prevent editing after approval
        if instance.status == 'approved':
            raise serializers.ValidationError("Cannot edit approved log")
        return super().update(instance, validated_data)