import json

from falcon import HTTP_200, HTTP_500

from src.dhl.requests.get_label import GetLabel


class Label:
    def __init__(self, dhl_client):
        self.item_to_print = GetLabel(client=dhl_client)

    def on_get(self, req, res):
        labels = self.item_to_print.request(shipment_id=req.media['shipment_id'], label_type=req.media['label_type'])

        res.status = HTTP_200
        if labels['success'] is False:
            res.status = HTTP_500

        res.body = json.dumps(labels)
