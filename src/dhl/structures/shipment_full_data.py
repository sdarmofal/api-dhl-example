from dataclasses import dataclass

from src.dhl.structures.address import Address
from src.dhl.structures.array_of_piece_definition import ArrayOfPieceDefinition
from src.dhl.structures.payment_data import PaymentData
from src.dhl.structures.receiver_address import ReceiverAddress
from src.dhl.structures.service_definition import ServiceDefinition
from src.dhl.structures.structure_base import StructureBase


@dataclass
class ShipmentFullData(StructureBase):
    shipper: Address
    receiver: ReceiverAddress
    piece_list: ArrayOfPieceDefinition
    payment: PaymentData
    service: ServiceDefinition
    shipment_date: str
    content: str
    comment: str = None
    reference: str = None
    shipment_id: int = None
    created: str = None
    order_status: str = None
    skip_restriction_check: bool = False

    def build_client_object(self, client_type):
        raise NotImplementedError("In this structure you should use build_client_object_recursive")

    def build_client_object_recursive(self, client_type_factory):
        return client_type_factory.ShipmentFullData(
            shipper=self.shipper.build_client_object(client_type_factory.Address),
            receiver=self.receiver.build_client_object(client_type_factory.ReceiverAddress),
            pieceList=self.piece_list.build_client_object_recursive(client_type_factory),
            payment=self.payment.build_client_object(client_type_factory.PaymentData),
            service=self.service.build_client_object(client_type_factory.ServiceDefinition),
            shipmentDate=self.shipment_date,
            skipRestrictionCheck=self.skip_restriction_check,
            comment=self.comment,
            content=self.content,
            reference=self.reference
        )
