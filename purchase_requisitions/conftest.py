import pytest
from pytest_factoryboy import register

from purchase_requisitions.requisitionform.models import Requisition
from purchase_requisitions.requisitionform.tests.factories import RequisitionFactory
from purchase_requisitions.users.models import User
from purchase_requisitions.users.tests.factories import UserFactory

register(RequisitionFactory)


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def requisition(db) -> Requisition:
    return RequisitionFactory()
