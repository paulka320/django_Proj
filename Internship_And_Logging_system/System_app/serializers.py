from rest_framework import serializers
from .models import CustomUser,EvaluationCriteria,Evaluation,InternshipPlacement,WeeklyLog


class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only =True)
    username =serializers.CharField(max_length=150)
    email = serializers.EmailField()
    role = serializers.CharField(max_length =30)

    def create(self,validated_data):
        return CustomUser.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.role = validated_data.get('role',instance.role)
        instance.save()
        return instance
    

    class EvaluationCriteriaserializer(serializers.Serializer):
        id = serializers.IntegerField(read_only = True)
        name = serializers.CharField(max_length=50)
        max_score = serializers.IntegerField()

        def create(self,validated_data):
            return EvaluationCriteria.objects.create(**validated_data)

        def update(self,instance,validated_data):
            instance.name = validated_data.get('username',instance.username)   