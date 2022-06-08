from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView

from purchase_requests.utils.mixins import DisplayTypeViewMixin, PageTitleViewMixin

from .forms import CreateRequestForm, UpdateRequestForm
from .models import Request


class RequestListView(PageTitleViewMixin, DisplayTypeViewMixin, ListView):
    model = Request
    template_name = "requestform/request_list.html"
    title = "Requests"
    display_type = "list"
    extra_context = {
        "verbose_fields": {
            field.name: field.verbose_name.title() for field in Request._meta.fields
        },
    }


class RequestListGridView(RequestListView):
    display_type = "grid"


class RequestCreateView(BSModalCreateView):
    model = Request
    form_class = CreateRequestForm
    success_message = "Success: Request was created."
    success_url = reverse_lazy("requests:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RequestCreateView, self).form_valid(form)


class RequestUpdateView(BSModalUpdateView):
    model = Request
    form_class = UpdateRequestForm
    success_message = "Success: Request was updated."
    success_url = reverse_lazy("requests:list")


class RequestDetailView(PageTitleViewMixin, DetailView):
    model = Request
    title = "Request Details"
    context_object_name = "p_request"


class RequestDeleteView(BSModalDeleteView):
    model = Request
    success_message = "Success: Request was deleted."
    success_url = reverse_lazy("requestform:list")
