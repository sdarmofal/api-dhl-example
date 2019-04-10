import json

from falcon import HTTP_500, HTTP_200

from src.dhl.requests.pickup import Pickup


class CourierPickup:
    def __init__(self, dhl_client):
        self.courier_pickup = Pickup(client=dhl_client)

    def on_post(self, req, res):
        pickup = self.courier_pickup.request(pickup_date=req.media['pickup_date'],
                                             pickup_time_from=req.media['hour_from'],
                                             pickup_time_to=req.media['hour_to'], shipment_id=req.media['shipment_id'])

        res.status = HTTP_200
        if pickup['success'] is False:
            res.status = HTTP_500

        res.body = json.dumps(pickup)
