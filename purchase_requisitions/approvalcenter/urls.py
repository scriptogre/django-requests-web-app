from django.urls import path

from purchase_requisitions.approvalcenter.views import ApprovalCenterView

app_name = "approval_center"

urlpatterns = [
    path("", view=ApprovalCenterView.as_view(), name="index"),
]
