from purchase_requisitions.requisitions.models import Requisition
from purchase_requisitions.requisitions.views import RequisitionListView


class ApprovalCenterView(RequisitionListView):
    title = "Approval Center"
    template_name = "approval_center/index.html"

    def get_queryset(self):
        return Requisition.objects.filter(
            status=Requisition.STATUS.PENDING, user=self.request.user
        )
