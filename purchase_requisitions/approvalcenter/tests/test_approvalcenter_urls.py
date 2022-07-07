import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_index(requisition):
    assert reverse("approval_center:index") == "/approval_center/"
    assert resolve("/approval_center/").view_name == "approval_center:index"
