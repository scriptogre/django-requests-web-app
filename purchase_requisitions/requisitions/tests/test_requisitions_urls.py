import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_index(requisition):
    assert reverse("requisitions:index") == "/requisitions/"
    assert resolve("/requisitions/").view_name == "requisitions:index"


def test_list_my(requisition):
    assert reverse("requisitions:list_my") == "/requisitions/my/"
    assert resolve("/requisitions/my/").view_name == "requisitions:list_my"


def test_approval_center(requisition):
    assert reverse("approval_center:index") == "/approval_center/"
    assert resolve("/approval_center/").view_name == "approval_center:index"


def test_list_all(requisition):
    assert reverse("requisitions:list_all") == "/requisitions/all/"
    assert resolve("/requisitions/all/").view_name == "requisitions:list_all"


def test_add(requisition):
    assert reverse("requisitions:add") == "/requisitions/add/"
    assert resolve("/requisitions/add/").view_name == "requisitions:add"


def test_detail(requisition):
    assert (
        reverse("requisitions:detail", kwargs={"pk": requisition.id})
        == f"/requisitions/{requisition.id}/"
    )
    assert (
        resolve(f"/requisitions/{requisition.id}/").view_name == "requisitions:detail"
    )


def test_update(requisition):
    assert (
        reverse("requisitions:update", kwargs={"pk": requisition.id})
        == f"/requisitions/{requisition.id}/update/"
    )
    assert (
        resolve(f"/requisitions/{requisition.id}/update/").view_name
        == "requisitions:update"
    )


def test_delete(requisition):
    assert (
        reverse("requisitions:delete", kwargs={"pk": requisition.id})
        == f"/requisitions/{requisition.id}/delete/"
    )
    assert (
        resolve(f"/requisitions/{requisition.id}/delete/").view_name
        == "requisitions:delete"
    )
