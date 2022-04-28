from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Request


class RequestsListView(ListView):

    model = Request

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class RequestCreateView(CreateView):
    model = Request
    fields = [
        "creator_name",
        "creator_email",
        "type",
        "description",
        "reason",
        "est_cost",
        "est_delivery",
        "attachment",
    ]


class RequestDetailView(DetailView):
    model = Request
    context_object_name = "request"


class RequestUpdateView(UpdateView):
    model = Request
    fields = [
        "creator_name",
        "creator_email",
        "type",
        "description",
        "reason",
        "est_cost",
        "est_delivery",
        "attachment",
    ]


class RequestDeleteView(DeleteView):
    model = Request
    success_url = reverse_lazy("list")
