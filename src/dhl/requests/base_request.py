class BaseRequest:
    def __init__(self, client):
        self.client = client
        self.type_factory = self.client.type_factory('ns0')

    def request(self, **kwargs):
        raise NotImplementedError
