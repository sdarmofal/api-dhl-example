import os
from typing import List

from zeep import helpers
from zeep.exceptions import Fault as SoapFault

from src.dhl.requests.base_request import BaseRequest
from src.dhl.structures.address import Address
from src.dhl.structures.array_of_piece_definition import ArrayOfPieceDefinition
from src.dhl.structures.array_of_shipment_full_data import ArrayOfShipmentFullData
from src.dhl.structures.auth_data import AuthData
from src.dhl.structures.payment_data import PaymentData
from src.dhl.structures.piece_definition import PieceDefinition
from src.dhl.structures.receiver_address import ReceiverAddress
from src.dhl.structures.service_definition import ServiceDefinition
from src.dhl.structures.shipment_full_data import ShipmentFullData


class CreateShipment(BaseRequest):
    def request(self, shipper_data: dict, receiver_data: dict, packages_data: list, service_data: dict,
                shipment_date: str, content: str):
        auth_data = self.build_auth_data()
        shipper = self.build_shipper(shipper_data)
        receiver = self.build_receiver(receiver_data)
        pieces = self.build_pieces(packages_data)
        payment = self.build_payment()
        service = self.build_service(service_data)

        array_of_shipment_full_data = self.build_array_of_shipment_full_data(shipper=shipper, receiver=receiver,
                                                                             pieces=pieces, payment=payment,
                                                                             service=service,
                                                                             shipment_date=shipment_date,
                                                                             content=content)

        try:
            result = self.client.service.createShipments(authData=auth_data, shipments=array_of_shipment_full_data)
        except SoapFault as e:
            return {
                "success": False,
                "response": e.message,
            }
        return {
            "success": True,
            "response": helpers.serialize_object(result)
        }

    @staticmethod
    def build_shipper(data: dict) -> Address:
        return Address(name=data['name'], postal_code=data['postalCode'], city=data['city'],
                       street=data['street'], house_number=data['houseNo'])

    @staticmethod
    def build_receiver(data: dict) -> ReceiverAddress:
        return ReceiverAddress(name=data['name'], postal_code=data['postalCode'], city=data['city'],
                               street=data['street'], house_number=data['houseNo'], country=data['country'])

    @staticmethod
    def build_pieces(packages: List[dict]):
        pieces = [PieceDefinition(**piece) for piece in packages]
        return ArrayOfPieceDefinition(items=pieces)

    @staticmethod
    def build_payment() -> PaymentData:
        return PaymentData(payment_method='BANK_TRANSFER', payer_type='USER', account_number=os.getenv('DHL.SAP', None))

    @staticmethod
    def build_service(data: dict) -> ServiceDefinition:
        return ServiceDefinition(**data)

    def build_auth_data(self):
        auth_data = AuthData()
        return auth_data.build_client_object(self.type_factory.AuthData)

    def build_array_of_shipment_full_data(self, shipper: Address, receiver: ReceiverAddress,
                                          pieces: ArrayOfPieceDefinition, payment, service, shipment_date, content):
        shipment_full_data = ShipmentFullData(shipper=shipper, receiver=receiver, piece_list=pieces, payment=payment,
                                              service=service, shipment_date=shipment_date, content=content)

        array_of_shipment_full_data = ArrayOfShipmentFullData(items=[shipment_full_data])
        return array_of_shipment_full_data.build_client_object_recursive(self.type_factory)
