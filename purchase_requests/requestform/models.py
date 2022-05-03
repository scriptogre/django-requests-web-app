from django.db import models
from django.urls import reverse
from model_utils import Choices
from model_utils.fields import StatusField


class Request(models.Model):

    STATUS = Choices("APPROVED", "PENDING", "REJECTED")
    BUDGET_CHOICES = Choices("Project", "Department")
    TYPE_CHOICES = Choices("Item", "Service")

    creator_name = models.CharField(max_length=150)
    creator_email = models.EmailField()
    type = models.CharField(
        max_length=7, choices=TYPE_CHOICES, default=TYPE_CHOICES.Item
    )
    description = models.TextField(max_length=256, blank=True, null=True)
    reason = models.TextField(max_length=256)
    est_cost = models.DecimalField(max_digits=6, decimal_places=2)
    est_delivery = models.DateField()
    attachment = models.FileField(upload_to="uploads/%Y/%m/%d/", blank=True, null=True)
    budget = models.CharField(
        max_length=10, choices=BUDGET_CHOICES, blank=True, null=True
    )
    status = StatusField(choices=STATUS, default=STATUS.PENDING, db_index=True)

    def get_absolute_url(self):
        return reverse("requests:detail", kwargs={"pk": self.pk})
