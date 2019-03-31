import falcon

from src.api.resources.shipment import Shipment
from src.api.resources.version import Version
from src.dhl.dhl_client import DHLClient

api = falcon.API()

dhl_client = DHLClient().client

api.add_route('/version', Version(dhl_client=dhl_client))
api.add_route('/shipment', Shipment(dhl_client=dhl_client))
