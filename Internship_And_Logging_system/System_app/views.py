from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CustomUser, InternshipPlacement, WeeklyLog, EvaluationCriteria, Evaluation
from .serializers import (
    CustomUserSerializer,
    InternshipPlacementSerializer,
    WeeklyLogSerializer,
    EvaluationCriteriaSerializer,
    EvaluationSerializer
)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class InternshipPlacementViewSet(viewsets.ModelViewSet):
    queryset = InternshipPlacement.objects.all()
    serializer_class = InternshipPlacementSerializer


class WeeklyLogViewSet(viewsets.ModelViewSet):
    queryset = WeeklyLog.objects.all()
    serializer_class = WeeklyLogSerializer

class EvaluationCriteriaViewSet(viewsets.ModelViewSet):
    queryset = EvaluationCriteria.objects.all()
    serializer_class = EvaluationCriteriaSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer