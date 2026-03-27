from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
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
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.User.role =='Administrator':
            return CustomUser.objects.all()
        return CustomUser.objects.none()


class InternshipPlacementViewSet(viewsets.ModelViewSet):
    queryset = InternshipPlacement.objects.all()
    serializer_class = InternshipPlacementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if CustomUser.role =="Student":
            return InternshipPlacement.objects.filter(students=CustomUser)
        elif CustomUser.role =='Adminstrator':
            return InternshipPlacement.objects.all()
        elif CustomUser.role=='Supervisor':
            return InternshipPlacement.objects.all()
        elif CustomUser.role =='Academic_Supervisor':
            return InternshipPlacement.objects.all()
        return InternshipPlacement.objects.none()


class WeeklyLogViewSet(viewsets.ModelViewSet):
    queryset = WeeklyLog.objects.all()
    serializer_class = WeeklyLogSerializer

class EvaluationCriteriaViewSet(viewsets.ModelViewSet):
    queryset = EvaluationCriteria.objects.all()
    serializer_class = EvaluationCriteriaSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer