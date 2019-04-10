from dataclasses import dataclass

from src.dhl.structures.structure_base import StructureBase


@dataclass
class ItemToPrint(StructureBase):
    label_type: str
    shipment_id: int

    LABEL_TYPES = ('BLP', 'ZBLP', 'LP')

    def build_client_object(self, client_type):
        if self.label_type not in self.LABEL_TYPES:
            raise AttributeError("Incorrect label_type")
        return client_type(labelType=self.label_type, shipmentId=self.shipment_id)
