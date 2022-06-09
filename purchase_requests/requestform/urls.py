from django.urls import path

from purchase_requests.requestform.views import (
    MyRequestListView,
    PendingRequestListView,
    RequestCreateView,
    RequestDeleteView,
    RequestDetailView,
    RequestUpdateView,
)

app_name = "requestform"
urlpatterns = [
    path("", view=MyRequestListView.as_view(), name="my_requests"),
    path("my", view=MyRequestListView.as_view(), name="my_requests"),
    path(
        "my/<slug:display_type>", view=MyRequestListView.as_view(), name="my_requests"
    ),
    path("pending", view=PendingRequestListView.as_view(), name="pending_requests"),
    path(
        "pending/<slug:display_type>",
        view=PendingRequestListView.as_view(),
        name="pending_requests",
    ),
    path("add", view=RequestCreateView.as_view(), name="add"),
    path("<int:pk>", view=RequestDetailView.as_view(), name="detail"),
    path("<int:pk>/update", view=RequestUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", view=RequestDeleteView.as_view(), name="delete"),
]
