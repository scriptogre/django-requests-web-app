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

from purchase_requests.utils.mixins import DisplayTypeViewMixin, PageTitleViewMixin

from .forms import CreateRequestForm, UpdateRequestForm
from .models import Request


class RequestListView(
    PageTitleViewMixin, DisplayTypeViewMixin, LoginRequiredMixin, ListView
):
    model = Request
    template_name = "requestform/request_list/request_list.html"
    extra_context = {
        "verbose_fields": {
            field.name: field.verbose_name.title() for field in Request._meta.fields
        },
    }

    def dispatch(self, request, *args, **kwargs):
        self.display_type = kwargs.get("display_type", "datatable")
        return super().dispatch(request, *args, **kwargs)


class MyRequestListView(RequestListView):
    title = "My Requests"

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)


class PendingRequestListView(RequestListView):
    title = "Pending Requests"

    def get_queryset(self):
        return Request.objects.filter(status=Request.STATUS.PENDING)


class RequestCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Request
    form_class = CreateRequestForm
    success_message = "Success: Request was created."
    success_url = reverse_lazy("requests:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RequestCreateView, self).form_valid(form)


class RequestUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Request
    form_class = UpdateRequestForm
    success_message = "Success: Request was updated."
    success_url = reverse_lazy("requests:my_requests")

    def get_success_url(self):
        if "display_type" in self.kwargs:
            display_type = self.kwargs["display_type"]
        else:
            display_type = "datatable"
        return reverse_lazy("requests:my_requests", args=[display_type])


class RequestDetailView(PageTitleViewMixin, LoginRequiredMixin, DetailView):
    model = Request
    title = "Request Details"
    context_object_name = "p_request"


class RequestDeleteView(UserPassesTestMixin, LoginRequiredMixin, BSModalDeleteView):
    model = Request
    success_message = "Success: Request was deleted."
    success_url = reverse_lazy("requests:my_requests")

    def test_func(self):
        p_request = self.model.objects.get(pk=self.kwargs["pk"])
        return self.request.user == p_request.user

    def handle_no_permission(self):
        return HttpResponse(
            """
            <div class="modal-header">
                <h5 class="modal-title">Permission Denied</h5>
            </div>
            <div class="modal-body">
                <p>Can't delete someone else's requests.</p>
            </div>
            """
        )
