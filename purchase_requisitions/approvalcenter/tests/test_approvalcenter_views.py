import pytest

from purchase_requisitions.requisitions.models import Requisition
from purchase_requisitions.requisitions.tests.factories import RequisitionFactory


@pytest.fixture()
def already_existing_requisitions():
    return RequisitionFactory.create_batch(size=5)


@pytest.mark.django_db
def test_approval_center_context(admin_client, already_existing_requisitions):
    """
    Checks if Pending Requisitions context contains only pending entries
    """
    context = admin_client.get("/approval_center/").context_data
    # TODO: Also check if objects returned are the user's objects
    assert set(context["requisition_list"]) == set(
        Requisition.objects.filter(status=Requisition.STATUS.PENDING)
    )
