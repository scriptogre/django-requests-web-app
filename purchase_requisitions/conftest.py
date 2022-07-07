import pytest
from pytest_factoryboy import register

from purchase_requisitions.requisitions.models import Requisition
from purchase_requisitions.requisitions.tests.factories import RequisitionFactory
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


@pytest.fixture(autouse=True)
def whitenoise_autorefresh(settings):
    """
    Get rid of whitenoise "No directory at" warning, as it's not helpful when running tests.

    Related:
        - https://github.com/evansd/whitenoise/issues/215
        - https://github.com/evansd/whitenoise/issues/191
        - https://github.com/evansd/whitenoise/commit/4204494d44213f7a51229de8bc224cf6d84c01eb
    """
    settings.WHITENOISE_AUTOREFRESH = True
