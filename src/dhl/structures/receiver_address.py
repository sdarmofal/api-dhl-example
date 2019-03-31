from dataclasses import dataclass


@dataclass
class ReceiverAddress:
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
