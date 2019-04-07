from dataclasses import dataclass

from src.dhl.structures.structure_base import StructureBase


@dataclass
class PieceDefinition(StructureBase):
    type: str
    width: int
    height: int
    length: int
    weight: int
    quantity: int
    non_standard: bool = False
    euro_return: bool = False
    blp_piece_id: str = None

    def build_client_object(self, client_type):
        return client_type(type=self.type, width=self.width, height=self.height, length=self.length, weight=self.weight,
                           quantity=self.quantity, nonStandard=self.non_standard, euroReturn=self.euro_return,
                           blpPieceId=self.blp_piece_id)
