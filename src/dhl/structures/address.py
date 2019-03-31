from dataclasses import dataclass

from src.dhl.structures.structure_base import StructureBase


@dataclass
class Address(StructureBase):
    name: str
    postal_code: str
    city: str
    street: str
    house_number: str
    apartment_number: str = None
    contact_person: str = None
    contact_phone: str = None
    contact_email: str = None

    def build_client_object(self, client_type):
        client_type(name=self.name, postalCode=self.postal_code, city=self.city, street=self.street,
                    houseNumber=self.house_number, apartmentNumber=self.apartment_number,
                    contactPerson=self.contact_person, contactPhone=self.contact_phone,
                    contactEmail=self.contact_person)
