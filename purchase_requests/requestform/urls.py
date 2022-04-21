from django.urls import path

from purchase_requests.requestform.views import RequestsListView

app_name = "requestform"

urlpatterns = [
    path("", view=RequestsListView.as_view(), name="requests-list"),
]
