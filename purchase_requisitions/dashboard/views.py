from django.contrib.auth import get_user_model
from django.views.generic import ListView

from purchase_requisitions.requisitionform.models import Requisition
from purchase_requisitions.utils.mixins import PageTitleViewMixin


class DashboardView(PageTitleViewMixin, ListView):
    model = Requisition
    template_name = "dashboard/dashboard.html"
    title = "Dashboard"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context.update(
            {
                "total_count": Requisition.objects.all().count(),
                "approved_count": Requisition.objects.approved().count(),
                "pending_count": Requisition.objects.pending().count(),
                "rejected_count": Requisition.objects.rejected().count(),
                "latest_requisitions": Requisition.objects.order_by("-id")[:5:-1],
                "users": get_user_model().objects.all(),
                "verbose_fields": {
                    field.name: field.verbose_name.title()
                    for field in Requisition._meta.fields
                },
                "approved_percentage": Requisition.objects.approved().count()
                * 100
                / Requisition.objects.all().count()
                if Requisition.objects.all().count()
                else 0,
                "pending_percentage": Requisition.objects.pending().count()
                * 100
                / Requisition.objects.all().count()
                if Requisition.objects.all().count()
                else 0,
                "rejected_percentage": Requisition.objects.rejected().count()
                * 100
                / Requisition.objects.all().count()
                if Requisition.objects.all().count()
                else 0,
            }
        )
        return context
