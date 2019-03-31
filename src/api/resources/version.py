import json

from falcon import HTTP_200

from src.dhl.requests.get_version import GetVersion


class Version:
    def __init__(self, dhl_client):
        self.get_version = GetVersion(client=dhl_client)

    def on_get(self, req, res):
        version = self.get_version.request()

        res.status = HTTP_200
        res.body = json.dumps({
            'version': version,
        })
