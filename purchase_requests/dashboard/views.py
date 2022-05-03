from django.views.generic import TemplateView

from purchase_requests.requestform.models import Request


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_requests"] = Request.objects.order_by("-id")[:5:-1]
        context["total_requests"] = Request.objects.count()
        context["pending_requests"] = Request.objects.filter(
            status=Request.STATUS.PENDING
        ).count()
        context["pending_requests_percentage"] = int(
            context["pending_requests"] * 100 / context["total_requests"]
        )
        context["approved_requests"] = Request.objects.filter(
            status=Request.STATUS.APPROVED
        ).count()
        context["approved_requests_percentage"] = int(
            (context["approved_requests"] * 100) / context["total_requests"]
        )
        context["rejected_requests"] = Request.objects.filter(
            status=Request.STATUS.REJECTED
        ).count()
        context["rejected_requests_percentage"] = int(
            (context["rejected_requests"] * 100) / context["total_requests"]
        )
        return context
