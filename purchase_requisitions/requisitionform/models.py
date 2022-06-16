from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from model_utils import Choices
from model_utils.fields import StatusField

from purchase_requisitions.models import TimeStampedModel
from purchase_requisitions.users.models import User


class RequisitionQuerySet(models.QuerySet):
    def approved(self):
        return self.filter(status=Requisition.STATUS.APPROVED)

    def pending(self):
        return self.filter(status=Requisition.STATUS.PENDING)

    def rejected(self):
        return self.filter(status=Requisition.STATUS.REJECTED)


class Requisition(TimeStampedModel):
    REQUEST_TYPE = Choices(
        ("ITEM", _("Item")),
        ("SERVICE", _("Service")),
        ("WORK_ORDER", _("Work Order")),
    )
    BUDGET = Choices(
        ("PROJECT", _("Project")),
        ("DEPARTMENT", _("Department")),
    )
    STATUS = Choices(
        ("APPROVED", _("Approved")),
        ("PENDING", _("Pending")),
        ("REJECTED", _("Rejected")),
    )

    status = StatusField(
        verbose_name="Status", choices=STATUS, default=STATUS.PENDING, db_index=True
    )

    creator_name = models.CharField(verbose_name="Name", max_length=150)
    creator_email = models.EmailField(verbose_name="Email")
    requisition_type = models.CharField(
        verbose_name="Requisition Type",
        max_length=10,
        choices=REQUEST_TYPE,
        default=REQUEST_TYPE.ITEM,
    )
    description = models.TextField(
        verbose_name="Description", max_length=256, blank=True, null=True
    )
    reason = models.TextField(verbose_name="Reason", max_length=256)
    est_cost = models.DecimalField(
        verbose_name="Estimated Cost", max_digits=6, decimal_places=2
    )
    est_delivery = models.DateField(verbose_name="Estimated Delivery Date")
    attachment = models.FileField(
        verbose_name="Attachment", upload_to="uploads/%Y/%m/%d/", blank=True
    )
    budget = models.CharField(
        verbose_name="Budget", max_length=10, choices=BUDGET, blank=True, null=True
    )

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    objects = RequisitionQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("requisitions:detail", kwargs={"pk": self.pk})
