from django.db import models
from django_fsm import FSMField, transition


class Request(models.Model):

    REQUEST_TYPE_CHOICES = [("SRV", "Service"), ("ITM", "Item")]
    BUDGET_CHOICES = [("PRJ", "Project"), ("DEP", "Department")]

    state = FSMField(default="new")

    @transition(field=state, source="new", target="pending_dept_approval")
    def choose_department_budget(self):
        # Notify Line Manager
        pass

    @transition(field=state, source="new", target="pending_pm_approval")
    def choose_project_budget(self):
        # Notify PM
        pass

    @transition(
        field=state, source="pending_dept_approval", target="pending_ceo_approval"
    )
    def approve_department_budget(self):
        # Notify RAM
        # Notify CEO
        pass

    @transition(
        field=state, source="pending_pm_approval", target="pending_ceo_approval"
    )
    def approve_project_budget(self):
        # Notify RAM
        # Notify CEO
        pass

    @transition(field=state, source="pending_ceo_approval", target="approved")
    def approve_from_ceo(self):
        # Notify PR
        pass

    @transition(
        field=state,
        source={"pending_dept_approval", "pending_pm_approval", "pending_ceo_approval"},
        target="rejected",
    )
    def reject(self):
        # Notify request creator
        pass

    @transition(field=state, source="new", target="new")
    def notify_new_request(self):
        # Better to fire whenever a new model is created
        pass

    creator_name = models.CharField(max_length=150)
    creator_email = models.EmailField()
    type = models.CharField(max_length=3, choices=REQUEST_TYPE_CHOICES, default="ITM")
    description = models.TextField(max_length=256)
    reason = models.TextField(max_length=256)
    est_cost = models.DecimalField(max_digits=6, decimal_places=2)
    est_delivery = models.DateField()
    attachment = models.FileField(upload_to="uploads/%Y/%m/%d/")

    budget_from = models.CharField(max_length=3, choices=BUDGET_CHOICES, default="DEP")

    is_budget_approved = models.BooleanField()
