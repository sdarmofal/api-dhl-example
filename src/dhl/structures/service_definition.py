from dataclasses import dataclass

from src.dhl.structures.structure_base import StructureBase


@dataclass
class ServiceDefinition(StructureBase):
    product: str
    delivery_evening: bool = False
    delivery_on_saturday: bool = False

    def build_client_object(self, client_type):
        return client_type(product=self.product, deliveryEvening=self.delivery_evening,
                           deliveryOnSaturday=self.delivery_on_saturday)
