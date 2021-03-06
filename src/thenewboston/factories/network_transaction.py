from factory import Faker, Iterator
from factory.django import DjangoModelFactory

from ..constants.network import ACCEPTED_FEE_LIST, MAX_POINT_VALUE, MIN_POINT_VALUE, VERIFY_KEY_LENGTH
from ..models.network_transaction import NetworkTransaction


class NetworkTransactionFactory(DjangoModelFactory):
    amount = Faker('pyint', max_value=MAX_POINT_VALUE, min_value=MIN_POINT_VALUE)
    fee = Iterator(ACCEPTED_FEE_LIST + [''])
    recipient = Faker('text', max_nb_chars=VERIFY_KEY_LENGTH)

    class Meta:
        model = NetworkTransaction
