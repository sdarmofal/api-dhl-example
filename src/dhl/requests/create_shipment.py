import os
from typing import List

from zeep.exceptions import Fault as SoapFault

from src.dhl.requests.base_request import BaseRequest
from src.dhl.structures.address import Address
from src.dhl.structures.auth_data import AuthData
from src.dhl.structures.payment_data import PaymentData
from src.dhl.structures.piece_definition import PieceDefinition
from src.dhl.structures.receiver_address import ReceiverAddress
from src.dhl.structures.service_definition import ServiceDefinition


class CreateShipment(BaseRequest):
    def __init__(self, client):
        self.client = client
        self.type_factory = self.client.type_factory('ns0')

    def request(self, shipper_data: dict, receiver_data: dict, packages_data: list, service_data: dict,
                shipment_date: str, content: str):
        auth_data = self.build_auth_data()
        shipper = self.build_shipper(shipper_data)
        receiver = self.build_receiver(receiver_data)
        pieces = self.build_pieces(packages_data)
        payment = self.build_payment()
        service = self.build_service(service_data)

        # full_data = ShipmentFullData()
        try:
            result = self.client.service.createShipments(authData=auth_data, shipments=[])
        except SoapFault as e:
            result = {
                "success": False,
                "error": e.message,
            }
        return result

    def build_shipper(self, data: dict) -> Address:
        shipper = Address(name=data['name'], postal_code=data['postalCode'], city=data['city'],
                          street=data['street'], house_number=data['houseNo'])
        return shipper.build_client_object(self.type_factory.AddressData)

    @staticmethod
    def build_receiver(data: dict) -> ReceiverAddress:
        return ReceiverAddress(name=data['name'], postal_code=data['postalCode'], city=data['city'],
                               street=data['street'], house_number=data['houseNo'], country=data['country'])

    @staticmethod
    def build_pieces(packages: List[dict]) -> List[PieceDefinition]:
        return [PieceDefinition(**piece) for piece in packages]

    @staticmethod
    def build_payment() -> PaymentData:
        return PaymentData(payment_method='BANK_TRANSFER', payer_type='USER', account_number=os.getenv('DHL.SAP', None))

    @staticmethod
    def build_service(data: dict) -> ServiceDefinition:
        return ServiceDefinition(**data)

    def build_auth_data(self):
        auth_data = AuthData()
        return auth_data.build_client_object(self.type_factory.AuthData)
