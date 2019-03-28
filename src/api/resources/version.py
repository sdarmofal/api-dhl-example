import json

from falcon import HTTP_200


class Version:
    def __init__(self, dhl_client):
        self.client = dhl_client

    def on_get(self, req, res):
        version = self.client.service.getVersion()

        res.status = HTTP_200
        res.body = json.dumps({
            'version': version,
        })
