from dataclasses import dataclass

from src.dhl.structures.structure_base import StructureBase


@dataclass
class ArrayOfPieceDefinition(StructureBase):
    items: list

    def build_client_object(self, client_type):
        raise NotImplementedError("In this structure you should use build_client_object_recursive")

    def build_client_object_recursive(self, client_type_factory):
        items = [item.build_client_object(client_type_factory.PieceDefinition) for item in self.items]
        return client_type_factory.ArrayOfPiecedefinition(item=items)
