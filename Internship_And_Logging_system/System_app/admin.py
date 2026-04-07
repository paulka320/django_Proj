from django.contrib import admin
from .models import CustomUser, InternshipPlacement, WeeklyLog, Evaluation, EvaluationCriteria
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')


@admin.register(InternshipPlacement)
class InternshipPlacementAdmin(admin.ModelAdmin):
    list_display = ('student', 'company_name', 'start_date', 'end_date')


@admin.register(WeeklyLog)
class WeeklyLogAdmin(admin.ModelAdmin):
    list_display = ('student', 'week_number', 'status')
    search_fields = ('student__username',)
    list_filter = ('status',)


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('student', 'criteria', 'score')


@admin.register(EvaluationCriteria)
class EvaluationCriteriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'max_score')
