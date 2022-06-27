import pytest
from factories import RequisitionFactory

from purchase_requisitions.requisitionform.models import Requisition

pytestmark = pytest.mark.django_db


def test_requisition_get_absolute_url(requisition: Requisition):
    assert requisition.get_absolute_url() == f"/requisitions/{requisition.id}/"


@pytest.mark.parametrize(
    "status, queryset, validity",
    [
        ("APPROVED", Requisition.objects.approved(), True),
        ("PENDING", Requisition.objects.approved(), False),
        ("REJECTED", Requisition.objects.approved(), False),
        ("APPROVED", Requisition.objects.pending(), False),
        ("PENDING", Requisition.objects.pending(), True),
        ("REJECTED", Requisition.objects.pending(), False),
        ("APPROVED", Requisition.objects.rejected(), False),
        ("PENDING", Requisition.objects.rejected(), False),
        ("REJECTED", Requisition.objects.rejected(), True),
    ],
)
def test_querysets(status, queryset, validity):
    assert (RequisitionFactory(status=status) in queryset) == validity
