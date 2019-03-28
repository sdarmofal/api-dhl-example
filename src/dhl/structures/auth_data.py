from dataclasses import dataclass


@dataclass
class AuthData:
    username: str
    password: str
