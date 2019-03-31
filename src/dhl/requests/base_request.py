class BaseRequest:
    def __init__(self, client):
        self.client = client

    def request(self, **kwargs):
        raise NotImplementedError
