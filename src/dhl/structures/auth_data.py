import os
from dataclasses import dataclass

from src.dhl.structures.structure_base import StructureBase


@dataclass
class AuthData(StructureBase):
    username: str = os.getenv('DHL.user', None)
    password: str = os.getenv('DHL.pass', None)

    def build_client_object(self, client_type):
        return client_type(username=self.username, password=self.password)




