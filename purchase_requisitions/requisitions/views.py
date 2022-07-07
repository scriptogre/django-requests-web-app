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

from purchase_requisitions.utils.mixins import PageTitleMixin

from .forms import CreateRequisitionForm, UpdateRequisitionForm
from .models import Requisition


class RequisitionListView(PageTitleMixin, LoginRequiredMixin, ListView):
    model = Requisition
    template_name = "requisitions/requisition_list.html"
    extra_context = {
        "verbose_fields": {
            field.name: field.verbose_name.title() for field in Requisition._meta.fields
        },
    }


class MyRequisitionsView(RequisitionListView):
    title = "My Requisitions"

    def get_queryset(self):
        return Requisition.objects.filter(user=self.request.user)


class AllRequisitionsView(UserPassesTestMixin, RequisitionListView):
    title = "All Requisitions"

    def test_func(self):
        return self.request.user.is_superuser


class RequisitionCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Requisition
    form_class = CreateRequisitionForm
    success_message = "Success: Requisition was created."
    success_url = reverse_lazy("requisitions:list_my")

    def form_valid(self, form):
        """
        CreateRequisitionForm "user" field set to POST request's user
        """
        form.instance.user = self.request.user
        return super(RequisitionCreateView, self).form_valid(form)


class RequisitionUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Requisition
    form_class = UpdateRequisitionForm
    success_message = "Success: Requisition was updated."
    success_url = reverse_lazy("requisitions:list_my")


class RequisitionDetailView(PageTitleMixin, LoginRequiredMixin, DetailView):
    model = Requisition
    title = "Requisition Details"
    context_object_name = "requisition"


class RequisitionDeleteView(UserPassesTestMixin, LoginRequiredMixin, BSModalDeleteView):
    model = Requisition
    success_message = "Success: Requisition was deleted."
    success_url = reverse_lazy("requisitions:list_my")

    def test_func(self):
        """
        DELETE request's user == Requisition's "user" field
        """
        entry = self.model.objects.get(pk=self.kwargs["pk"])
        return self.request.user == entry.user

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
