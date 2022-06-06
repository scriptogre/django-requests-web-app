from django.urls import path

from purchase_requests.requestform.views import (
    RequestCreateView,
    RequestDeleteView,
    RequestDetailView,
    RequestListGridView,
    RequestListView,
    RequestUpdateView,
)

app_name = "requestform"
urlpatterns = [
    path("", view=RequestListView.as_view(), name="list"),
    path("grid/", view=RequestListGridView.as_view(), name="grid_list"),
    path("add/", view=RequestCreateView.as_view(), name="add"),
    path("<int:pk>/", view=RequestDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", view=RequestUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", view=RequestDeleteView.as_view(), name="delete"),
]
