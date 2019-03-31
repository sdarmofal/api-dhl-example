from src.dhl.requests.base_request import BaseRequest


class GetVersion(BaseRequest):
    def request(self):
        return self.client.service.getVersion()
