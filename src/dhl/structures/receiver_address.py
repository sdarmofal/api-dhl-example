from dataclasses import dataclass

from src.dhl.structures.structure_base import StructureBase


@dataclass
class ReceiverAddress(StructureBase):
    name: str
    postal_code: str
    city: str
    street: str
    house_number: str
    country: str
    apartment_number: str = None
    contact_person: str = None
    contact_phone: str = None
    contact_email: str = None
    is_packstation: bool = False
    is_postfiliale: bool = False
    postnummer: str = None

    def build_client_object(self, client_type):
        return client_type(name=self.name, postalCode=self.postal_code, city=self.city, street=self.street,
                           houseNumber=self.house_number, country=self.country, apartmentNumber=self.apartment_number,
                           isPackstation=self.is_packstation, isPostfiliale=self.is_postfiliale,
                           postnummer=self.postnummer)
