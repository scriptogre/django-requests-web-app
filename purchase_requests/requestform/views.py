# from django.shortcuts import get_object_or_404, redirect, render
# from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.views.generic.list import ListView

from .models import Request

# from django_fsm import can_proceed


class RequestsListView(ListView):

    model = Request

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


# def choose_dept_budget_view(request, post_id):
#     purchase_req = get_object_or_404(Request, pk=post_id)
#     if not can_proceed(purchase_req.choose_department_budget):
#         raise PermissionDenied
#
#     purchase_req.choose_department_budget()
#     purchase_req.save()
#     return redirect('/')
#
#
# def choose_pm_budget_view(request, post_id):
#     purchase_req = get_object_or_404(Request, pk=post_id)
#     if not can_proceed(purchase_req.choose_project_budget):
#         raise PermissionDenied
#
#     purchase_req.choose_project_budget()
#     purchase_req.save()
#     return redirect('/')
#
