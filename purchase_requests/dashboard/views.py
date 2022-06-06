from django.contrib.auth import get_user_model
from django.views.generic import ListView

from purchase_requests.requestform.models import Request
from purchase_requests.utils.mixins import PageTitleViewMixin


class DashboardView(PageTitleViewMixin, ListView):
    model = Request
    template_name = "dashboard/dashboard.html"
    title = "Dashboard"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context.update(
            {
                "total_count": Request.objects.all().count(),
                "approved_count": Request.objects.approved().count(),
                "pending_count": Request.objects.pending().count(),
                "rejected_count": Request.objects.rejected().count(),
                "latest_requests": Request.objects.order_by("-id")[:5:-1],
                "users": get_user_model().objects.all(),
                "verbose_fields": {
                    field.name: field.verbose_name.title()
                    for field in Request._meta.fields
                },
                "approved_percentage": Request.objects.approved().count()
                * 100
                / Request.objects.all().count()
                if Request.objects.all().count()
                else 0,
                "pending_percentage": Request.objects.pending().count()
                * 100
                / Request.objects.all().count()
                if Request.objects.all().count()
                else 0,
                "rejected_percentage": Request.objects.rejected().count()
                * 100
                / Request.objects.all().count()
                if Request.objects.all().count()
                else 0,
            }
        )
        return context
