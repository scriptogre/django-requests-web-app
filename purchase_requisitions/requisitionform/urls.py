from django.urls import path
from django.views.generic import RedirectView

from purchase_requisitions.requisitionform.views import (
    AllRequisitionsView,
    MyRequisitionsView,
    ApprovalCenterView,
    RequisitionCreateView,
    RequisitionDeleteView,
    RequisitionDetailView,
    RequisitionUpdateView,
)

app_name = "requisitionform"
urlpatterns = [
    path("", view=RedirectView.as_view(url="my/", permanent=True), name="index"),
    path("my/", view=MyRequisitionsView.as_view(), name="list_my"),
    path("pending/", view=ApprovalCenterView.as_view(), name="list_pending"),
    path("all/", view=AllRequisitionsView.as_view(), name="list_all"),
    path("add/", view=RequisitionCreateView.as_view(), name="add"),
    path("<int:pk>/", view=RequisitionDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", view=RequisitionUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", view=RequisitionDeleteView.as_view(), name="delete"),
]
