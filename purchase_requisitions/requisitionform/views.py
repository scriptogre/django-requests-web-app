from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalUpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView

from purchase_requisitions.utils.mixins import DisplayTypeViewMixin, PageTitleViewMixin

from .forms import CreateRequisitionForm, UpdateRequisitionForm
from .models import Requisition


class RequisitionListView(
    PageTitleViewMixin, DisplayTypeViewMixin, LoginRequiredMixin, ListView
):
    model = Requisition
    template_name = "requisitionform/requisition_list/requisition_list.html"
    extra_context = {
        "verbose_fields": {
            field.name: field.verbose_name.title() for field in Requisition._meta.fields
        },
    }

    def dispatch(self, request, *args, **kwargs):
        """Get the display_type kwarg from url, defaults to datatable"""
        self.display_type = kwargs.get("display_type", "datatable")
        return super().dispatch(request, *args, **kwargs)


class AllRequisitionListView(UserPassesTestMixin, RequisitionListView):
    title = "All Requisitions"

    def test_func(self):
        return self.request.user.is_superuser


class MyRequisitionListView(RequisitionListView):
    title = "My Requisitions"

    def get_queryset(self):
        return Requisition.objects.filter(user=self.request.user)


class PendingRequisitionListView(RequisitionListView):
    title = "Pending Requisitions"

    def get_queryset(self):
        return Requisition.objects.filter(status=Requisition.STATUS.PENDING)


class RequisitionCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Requisition
    form_class = CreateRequisitionForm
    success_message = "Success: Requisition was created."
    success_url = reverse_lazy("requisitions:my_requisitions")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RequisitionCreateView, self).form_valid(form)


class RequisitionUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Requisition
    form_class = UpdateRequisitionForm
    success_message = "Success: Requisition was updated."

    def get_success_url(self):
        if "display_type" in self.kwargs:
            display_type = self.kwargs["display_type"]
        else:
            display_type = "datatable"
        return reverse_lazy(
            "requisitions:my_requisitions", kwargs={"display_type": display_type}
        )


class RequisitionDetailView(PageTitleViewMixin, LoginRequiredMixin, DetailView):
    model = Requisition
    title = "Requisition Details"
    context_object_name = "p_requisition"


class RequisitionDeleteView(UserPassesTestMixin, LoginRequiredMixin, BSModalDeleteView):
    model = Requisition
    success_message = "Success: Requisition was deleted."
    success_url = reverse_lazy("requisitions:my_requisitions")

    def test_func(self):
        p_requisition = self.model.objects.get(pk=self.kwargs["pk"])
        return self.request.user == p_requisition.user

    def handle_no_permission(self):
        return HttpResponse(
            """
            <div class="modal-header">
                <h5 class="modal-title">Permission Denied</h5>
            </div>
            <div class="modal-body">
                <p>Can't delete someone else's requisitions.</p>
            </div>
            """
        )
