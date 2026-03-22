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
    

class EvaluationCriteriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=50)
    max_score = serializers.IntegerField()

    def create(self,validated_data):
        return EvaluationCriteria.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('username',instance.username) 
        instance.max_score = validated_data.get('max_score',instance.max_score)

class WeeklyLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    student = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    week_number = serializers.IntegerField()
    activities = serializers.CharField(max_length=200,required=True,allow_blank=False)
    challenges = serializers.CharField(max_length=200,required=True,allow_blank=False)
    supervisor_comment = serializers.CharField(max_length=200,required = True,allow_blank =False)

    def create(self,validated_data):
        return WeeklyLog.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.student = validated_data.get('student',instance.student)
        instance.week_number = validated_data.get('week_number',instance.week_number)
        instance.activities = validated_data.get('activities',instance.activities)
        instance.challenges = validated_data.get('challenges',instance.challenges)

class EvaluationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    student = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    criteria = serializers.PrimaryKeyRelatedField(queryset=EvaluationCriteria.objects.all())
    score = serializers.IntegerField()

    def validated_score(self,value):
        if value < 0 :
            raise serializers.validationError("Score can not be negative")
        return value
    
    def create(self,validated_data):
        return Evaluation.objects.create(**validated_data)
    
class InternshipPlacementSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    student = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    supervisor = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    company_name=serializers.CharField(max_length=200)
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self,validated_data):
        return InternshipPlacement.objects.create(**validated_data)
  