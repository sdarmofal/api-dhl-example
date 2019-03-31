from dataclasses import dataclass
from typing import List

from src.dhl.structures.address import Address
from src.dhl.structures.payment_data import PaymentData
from src.dhl.structures.piece_definition import PieceDefinition
from src.dhl.structures.receiver_address import ReceiverAddress
from src.dhl.structures.service_definition import ServiceDefinition


@dataclass
class ShipmentFullData:
    shipper: Address
    receiver: ReceiverAddress
    piece_list: List[PieceDefinition]
    payment: PaymentData
    service: ServiceDefinition
    shipment_date: str
    skip_restriction_check: bool
    comment: str
    content: str
    reference: str
    shipment_id: int
    created: str
    order_status: str
