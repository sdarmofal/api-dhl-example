from dataclasses import dataclass

from src.dhl.structures.structure_base import StructureBase


@dataclass
class PaymentData(StructureBase):
    payment_method: str
    payer_type: str
    account_number: str = None
    costs_center: str = None

    def build_client_object(self, client_type):
        return client_type(paymentMethod=self.payment_method, payerType=self.payer_type,
                           accountNumber=self.account_number, costsCenter=self.costs_center)
