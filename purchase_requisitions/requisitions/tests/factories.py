from factory import SubFactory
from factory.django import DjangoModelFactory, ImageField
from faker import Faker

from purchase_requisitions.requisitions.models import Requisition
from purchase_requisitions.users.tests.factories import UserFactory

fake = Faker()


class RequisitionFactory(DjangoModelFactory):
    """
    Creates a new Requisition object,
    also creates a new User object which will be the creator of this Requisition
    """

    status = fake.random_element(x[0] for x in Requisition.STATUS)
    creator_name = fake.name()
    creator_email = fake.email(domain="tigermedgrp.com")
    requisition_type = fake.random_element(x[0] for x in Requisition.REQUISITION_TYPE)
    description = fake.paragraph(nb_sentences=4)
    reason = fake.paragraph(nb_sentences=1)
    est_cost = fake.random_int(min=0, max=5000)
    est_delivery = fake.date()
    attachment = ImageField(filename="attachment.jpg", format="JPEG")
    budget = fake.random_element(x[0] for x in Requisition.BUDGET)
    user = SubFactory(UserFactory)

    class Meta:
        model = Requisition
