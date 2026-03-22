from rest_framework import serializers
from .models import CustomUser,EvaluationCriteria,Evaluation,InternshipPlacement,WeeklyLog


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields='__all__'    

class EvaluationCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationCriteria
        fields = '__all__'

class WeeklyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyLog
        field = '__all__'


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

    def validated_score(self,value):
        if value < 0 :
            raise serializers.validationError("Score can not be negative")
        return value
    
    
class InternshipPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipPlacement
        fields ='__all__'