from django.contrib.admin import ModelAdmin, register

from purchase_requisitions.requisitionform.models import Requisition


@register(Requisition)
class MaterialRequisitionAdmin(ModelAdmin):
    icon_name = "person"
    # list_display = 'name', 'first_name', 'last_name'
