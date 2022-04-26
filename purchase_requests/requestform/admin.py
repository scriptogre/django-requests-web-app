from django.contrib.admin import ModelAdmin, register

from purchase_requests.requestform.models import Request


@register(Request)
class MaterialRequestAdmin(ModelAdmin):
    icon_name = "person"
    # list_display = 'name', 'first_name', 'last_name'
