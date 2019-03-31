import json

from falcon import HTTP_200, HTTP_500

from src.dhl.requests.create_shipment import CreateShipment


class Shipment:
    def __init__(self, dhl_client):
        self.create_shipment = CreateShipment(client=dhl_client)

    def on_post(self, req, res):
        shipment = self.create_shipment.request(shipper_data=req.media['shipper'], receiver_data=req.media['receiver'],
                                                packages_data=req.media['packages'], service_data=req.media['services'],
                                                shipment_date=req.media['shipment_date'], content=req.media['content'])

        res.status = HTTP_200
        if shipment['success'] is False:
            res.status = HTTP_500

        res.body = json.dumps(shipment)
