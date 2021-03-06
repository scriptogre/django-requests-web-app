from bootstrap_modal_forms.forms import BSModalModelForm
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Button, ButtonHolder, Div, Layout

from .models import Requisition


class ParentRequisitionForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

    class Meta:
        model = Requisition
        fields = [
            "creator_name",
            "creator_email",
            "requisition_type",
            "description",
            "reason",
            "est_cost",
            "est_delivery",
            "attachment",
        ]


class CreateRequisitionForm(ParentRequisitionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["creator_name"].initial = "John Doe"
        self.fields["creator_email"].initial = "john@doe.com"
        self.fields["description"].initial = "This might be a description"
        self.fields["reason"].initial = "This is an example reason"
        self.fields["est_cost"].initial = "123"
        self.fields["est_delivery"].initial = "2022-04-20"
        self.helper.form_id = "createRequisition"
        self.helper.layout = Layout(
            Div(
                HTML('<h5 class="modal-title">Create New Requisition</h5>'),
                HTML(
                    '<button type="button" class="close" data-bs-dismiss="modal" aria-label=Close>'
                    '<span aria-hidden="true">×</span>'
                    "</button>"
                ),
                css_class="modal-header",
            ),
            Div(
                FloatingField("creator_name"),
                FloatingField("creator_email"),
                FloatingField("requisition_type"),
                FloatingField("description"),
                FloatingField("reason"),
                FloatingField("est_cost"),
                FloatingField("est_delivery"),
                FloatingField("attachment"),
                css_class="modal-body",
            ),
            Div(
                ButtonHolder(
                    Button(
                        "close",
                        "Close",
                        type="button",
                        css_class="btn btn-default",
                        data_bs_dismiss="modal",
                    ),
                    HTML(
                        '<button type="submit" class="btn btn-primary">Create</button>'
                    ),
                ),
                css_class="modal-footer",
            ),
        )


class UpdateRequisitionForm(ParentRequisitionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_id = "updateRequisition"
        self.helper.layout = Layout(
            Div(
                HTML('<h5 class="modal-title">Update Requisition</h5>'),
                HTML(
                    '<button type="button" class="close" data-bs-dismiss="modal" aria-label=Close>'
                    '<span aria-hidden="true">×</span>'
                    "</button>"
                ),
                css_class="modal-header",
            ),
            Div(
                FloatingField("creator_name"),
                FloatingField("creator_email"),
                FloatingField("requisition_type"),
                FloatingField("description"),
                FloatingField("reason"),
                FloatingField("est_cost"),
                FloatingField("est_delivery"),
                FloatingField("attachment"),
                css_class="modal-body",
            ),
            Div(
                ButtonHolder(
                    Button(
                        "close",
                        "Close",
                        type="button",
                        css_class="btn btn-default",
                        data_bs_dismiss="modal",
                    ),
                    HTML(
                        '<button type="submit" class="btn btn-primary">Update</button>'
                    ),
                ),
                css_class="modal-footer",
            ),
        )
