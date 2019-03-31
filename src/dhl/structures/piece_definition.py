from dataclasses import dataclass


@dataclass
class PieceDefinition:
    type: str
    width: int
    height: int
    length: int
    weight: int
    quantity: int
    non_standard: bool = False
    euro_return: bool = False
    blp_piece_id: str = None
