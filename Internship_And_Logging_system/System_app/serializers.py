from rest_framework import serializers
from .models import CustomUser,EvaluationCriteria,Evaluation,InternshipPlacement,WeeklyLog


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields='__all__'    

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