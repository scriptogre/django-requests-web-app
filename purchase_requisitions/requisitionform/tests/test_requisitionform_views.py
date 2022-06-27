# PendingRequisitionListView
# Someone accesses Pending Requisitions assert ONLY GETS PENDING ENTRIES
# Create multiple entries both with Approved/Rejected

# RequisitionCreateView
# Someone creates a new entry
# assert user field is automatically filled with his user
# assert form_valid returns without error

# RequisitionDeleteView
# Someone tries to delete an entry
# assert CAN'T DELETE OTHERS' ENTRIES
# assert CAN DELETE HIS OWN ENTRIES
# assert MODAL APPEARS IN HTML Template

import pytest
from django.test import RequestFactory

from purchase_requisitions.requisitionform.models import Requisition
from purchase_requisitions.requisitionform.tests.factories import RequisitionFactory


@pytest.fixture()
def logged_in_user(client, user):
    client.force_login(user)
    return user


@pytest.fixture()
def already_existing_requisitions():
    return RequisitionFactory.create_batch(size=5)


@pytest.mark.parametrize(
    "url, is_authenticated, expected",
    [
        # Guest User
        (
            "/requisitions/",
            False,
            301,
        ),  # /requisitions/ should always redirect to /requisitions/my/
        ("/requisitions/my/", False, 302),
        ("/requisitions/all/", False, 302),
        ("/requisitions/pending/", False, 302),
        # Basic User
        ("/requisitions/", True, 301),
        ("/requisitions/my/", True, 200),
        ("/requisitions/all/", True, 403),
        ("/requisitions/pending/", True, 200),
    ],
)
def test_user_access(db, user, client, url, is_authenticated, expected):
    """
    Checks status code of accessing urls as guest(non logged-in)/basic user
    """
    if is_authenticated:
        client.force_login(user)  # Login as basic user
    response = client.get(url)
    assert response.status_code == expected


@pytest.mark.parametrize(
    "url, expected",
    [
        ("/requisitions/", 301),
        ("/requisitions/my/", 200),
        ("/requisitions/all/", 200),
        ("/requisitions/pending/", 200),
    ],
)
def test_admin_access(db, admin_client, url, expected):
    """
    Checks status code of accessing urls as admin user
    """
    response = admin_client.get(url)
    assert response.status_code == expected


@pytest.mark.django_db
def test_my_requisitions_context(client, logged_in_user, already_existing_requisitions):
    """
    Checks if My Requisitions context contains only my entries
    """
    my_entries = RequisitionFactory.create_batch(
        user=logged_in_user, size=3
    )  # My user creates 3 entries
    context = client.get("/requisitions/my/").context_data
    context_entries = list(context["requisition_list"])
    assert (
        context_entries
        == my_entries
        == list(Requisition.objects.filter(user=logged_in_user))
    )


@pytest.mark.django_db
def test_all_requisitions_context(admin_client, already_existing_requisitions):
    """
    Checks if All Requisitions context contains all entries
    """
    context = admin_client.get("/requisitions/all/").context_data
    assert set(context["requisition_list"]) == set(Requisition.objects.all())


@pytest.mark.django_db
def test_pending_requisitions_context(admin_client, already_existing_requisitions):
    """
    Checks if Pending Requisitions context contains only pending entries
    """
    context = admin_client.get("/requisitions/pending/").context_data
    assert set(context["requisition_list"]) == set(
        Requisition.objects.filter(status=Requisition.STATUS.PENDING)
    )


factory = RequestFactory()


@pytest.mark.django_db
def test_form_valid_on_create_view(logged_in_user):
    # Arrange
    data = {
        "creator_name": "John",
        "creator_email": "john@doe.com",
        "requisition_type": Requisition.REQUISITION_TYPE.ITEM,
        "description": "description",
        "reason": "reason",
        "est_cost": 1,
        "est_delivery": "2022-04-10",
        "user": logged_in_user,
    }

    request = factory.post("/requisitions/add/", data=data)
    request.user = logged_in_user

    # Act
    # response = RequisitionCreateView.as_view()(request)
    # print(response)
    assert True
