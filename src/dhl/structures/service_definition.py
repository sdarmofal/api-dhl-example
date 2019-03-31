from dataclasses import dataclass


@dataclass
class ServiceDefinition:
    product: str
    delivery_evening: bool = False
    delivery_on_saturday: bool = False
