from django.urls import path
from django.views.generic import RedirectView

from purchase_requisitions.requisitionform.views import (
    AllRequisitionListView,
    MyRequisitionListView,
    PendingRequisitionListView,
    RequisitionCreateView,
    RequisitionDeleteView,
    RequisitionDetailView,
    RequisitionUpdateView,
)

app_name = "requisitionform"
urlpatterns = [
    path("", view=RedirectView.as_view(url="my/", permanent=True)),
    path("my/", view=MyRequisitionListView.as_view(), name="my_requisitions"),
    path(
        "pending/",
        view=PendingRequisitionListView.as_view(),
        name="pending_requisitions",
    ),
    path("all/", view=AllRequisitionListView.as_view(), name="all_requisitions"),
    path("add/", view=RequisitionCreateView.as_view(), name="add"),
    path("<int:pk>/", view=RequisitionDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", view=RequisitionUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", view=RequisitionDeleteView.as_view(), name="delete"),
]
