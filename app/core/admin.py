from django.contrib import admin
from core.models import Indicator, StudentInfo


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ("scorecard_name", "step", "milestone",
                    "score", "narrative", "year")
    list_filter = ("scorecard_name", "year")
    search_fields = ["scorecard_name"]
    list_editable = ("step",
                     "score", "year")


@admin.register(StudentInfo)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['title']
