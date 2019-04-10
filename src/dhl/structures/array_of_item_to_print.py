from dataclasses import dataclass
from typing import List

from src.dhl.structures.item_to_print import ItemToPrint
from src.dhl.structures.structure_base import StructureBase


@dataclass
class ArrayOfItemToPrint(StructureBase):
    items: List[ItemToPrint]

    def build_client_object(self, client_type):
        raise NotImplementedError("In this structure you should use build_client_object_recursive")

    def build_client_object_recursive(self, client_type_factory):
        items = [item.build_client_object(client_type_factory.ItemToPrint) for item in self.items]
        return client_type_factory.ArrayOfItemtoprint(item=items)
