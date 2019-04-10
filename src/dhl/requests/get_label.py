from zeep import helpers
from zeep.exceptions import Fault as SoapFault

from src.dhl.requests.base_request import BaseRequest
from src.dhl.structures.auth_data import AuthData
from src.dhl.structures.item_to_print import ItemToPrint
from src.dhl.structures.array_of_item_to_print import ArrayOfItemToPrint


class GetLabel(BaseRequest):
    def request(self, shipment_id: int, label_type: str):
        auth_data = self.build_auth_data()

        try:
            items_to_print = self.build_items_to_print(shipment_id, label_type)
            result = self.client.service.getLabels(authData=auth_data, itemsToPrint=items_to_print)
        except SoapFault as e:
            return {
                "success": False,
                "response": e.message,
            }
        except AttributeError as e:
            return {
                "success": False,
                "response": e.args[0],
            }
        return {
            "success": True,
            "response": helpers.serialize_object(result)
        }

    def build_auth_data(self):
        auth_data = AuthData()
        return auth_data.build_client_object(self.type_factory.AuthData)

    def build_items_to_print(self, shipment_id: int, label_type: str):
        item = ItemToPrint(shipment_id=shipment_id, label_type=label_type)
        return ArrayOfItemToPrint(items=[item]).build_client_object_recursive(self.type_factory)
