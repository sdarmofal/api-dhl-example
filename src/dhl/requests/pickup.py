from zeep import helpers
from zeep.exceptions import Fault as SoapFault

from src.dhl.requests.base_request import BaseRequest
from src.dhl.structures.auth_data import AuthData


class Pickup(BaseRequest):

    def request(self, pickup_date: str, pickup_time_from: str, pickup_time_to: str, shipment_id):
        auth_data = self.build_auth_data()

        try:
            result = self.client.service.bookCourier(authData=auth_data, pickupDate=pickup_date,
                                                     pickupTimeFrom=pickup_time_from, pickupTimeTo=pickup_time_to,
                                                     shipmentIdList=[shipment_id])
        except SoapFault as e:
            return {
                "success": False,
                "response": e.message,
            }
        return {
            "success": True,
            "response": helpers.serialize_object(result)
        }

    def build_auth_data(self):
        auth_data = AuthData()
        return auth_data.build_client_object(self.type_factory.AuthData)
