from django.contrib.auth import get_user_model
from django.views.generic import ListView

from purchase_requests.requestform.models import Request


class DashboardView(ListView):
    model = Request
    template_name = "dashboard/dashboard.html"
    extra_context = {
        "total_count": Request.objects.all().count(),
        "approved_count": Request.objects.approved().count(),
        "pending_count": Request.objects.pending().count(),
        "rejected_count": Request.objects.rejected().count(),
        "latest_requests": Request.objects.order_by("-id")[:5:-1],
        "users": get_user_model().objects.all(),
        "verbose_fields": {
            field.name: field.verbose_name.title() for field in Request._meta.fields
        },
    }
    extra_context.update(
        {
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
