from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalDeleteView,
    BSModalUpdateView,
)
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .forms import CreateRequestForm, UpdateRequestForm
from .models import Request


class RequestListView(ListView):
    model = Request
    template_name = "requestform/request_list.html"
    extra_context = {
        "verbose_fields": {
            field.name: field.verbose_name.title() for field in Request._meta.fields
        },
    }


class RequestCreateView(BSModalCreateView):
    model = Request
    form_class = CreateRequestForm
    success_message = "Success: Request was created."
    success_url = reverse_lazy("requests:list")


class RequestUpdateView(BSModalUpdateView):
    model = Request
    form_class = UpdateRequestForm
    success_message = "Success: Request was updated."
    success_url = reverse_lazy("requests:list")


class RequestDetailView(DetailView):
    model = Request
    context_object_name = "request"


class RequestDeleteView(BSModalDeleteView):
    model = Request
    success_message = "Success: Request was deleted."
    success_url = reverse_lazy("requestform:list")
