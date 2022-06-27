import pytest
from django.views.generic import TemplateView

from purchase_requisitions.utils.mixins import PageTitleMixin


@pytest.fixture
def dummy_view():
    class Dummy(PageTitleMixin, TemplateView):
        template_name = "base.html"

    return Dummy()


@pytest.mark.django_db
def test_no_title(dummy_view):
    context = dummy_view.get_context_data()
    assert not context["title"]


@pytest.mark.django_db
def test_has_title(dummy_view):
    dummy_view.title = "some_title"
    context = dummy_view.get_context_data()
    assert context["title"] == "some_title"
