from django.views.generic import TemplateView

from purchase_requests.requestform.models import Request


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_requests"] = Request.objects.order_by("-id")[:5:-1]
        context["total_requests"] = Request.objects.count()
        return context
