import os

from zeep import Client


class DHLClient:
    def __init__(self):
        self.WSDL = os.getenv('DHL.WSDL', None)
        self.client = Client(wsdl=self.WSDL)
