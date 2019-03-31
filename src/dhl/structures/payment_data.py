from dataclasses import dataclass


@dataclass
class PaymentData:
    payment_method: str
    payer_type: str
    account_number: str = None
    costs_center: str = None
