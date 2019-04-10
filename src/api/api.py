import falcon

from src.api.resources.courier_pickup import CourierPickup
from src.api.resources.label import Label
from src.api.resources.shipment import Shipment
from src.api.resources.version import Version
from src.dhl.dhl_client import DHLClient

api = falcon.API()

dhl_client = DHLClient().client

api.add_route('/version', Version(dhl_client=dhl_client))
api.add_route('/shipment', Shipment(dhl_client=dhl_client))
api.add_route('/pickup', CourierPickup(dhl_client=dhl_client))
api.add_route('/label', Label(dhl_client=dhl_client))
