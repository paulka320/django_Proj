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
        if self.request.CustomUser.role =='Administrator':
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        #Students can only see their own logs
        if user.role == 'student':
            return WeeklyLog.objects.filter(student=user)
        
        #Supervisors and admins can see all logs
        elif user.role in ['supervisor', 'administrator', 'academic_supervisor']:
            return WeeklyLog.objects.all()
        
        return WeeklyLog.objects.none()
        
    def perform_create(self, serializer):
        if self.request.user.role != 'student':
            raise PermissionDenied("Only students can create weekly logs.")
            
        serializer.save(student=self.request.user)

class EvaluationCriteriaViewSet(viewsets.ModelViewSet):
    queryset = EvaluationCriteria.objects.all()
    serializer_class = EvaluationCriteriaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only the admin can manage the criteria
        if self.request.user.role == 'admin':
            return EvaluationCriteria.objects.all()
        return EvaluationCriteria.objects.none()



class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user

        if user.role =='student':
            return Evaluation.objects.filter(student=user)
        
        elif user.role in ['supervisor', 'administrator', 'academic_supervisor']:
            return Evaluation.objects.all()
        
        return Evaluation.objects.none()

    def perform_create(self,serializer):
        #only supervisor/admin can evaluate students
        if self.request.user.role not in ['supervisor', 'administrator', 'academic_supervisor']:
            raise PermissionDenied("Only supervisor/administrator can evaluate students")
        
        serializer.save()
    
    

