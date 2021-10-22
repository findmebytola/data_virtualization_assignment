from django.contrib import admin
from core.models import Indicator


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ("scorecard_name", "step", "milestone",
                    "score", "narrative", "year")
    list_filter = ("scorecard_name", "year")
    search_fields = ["scorecard_name"]
    list_editable = ("score", "narrative")
