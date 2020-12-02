import requests
from rest_api.endpoints.login import LoginEndpoint
from rest_api.endpoints.user import UserEndpoint


class RestApi(object):

    def __init__(self, configuration):
        self.cfg = configuration

        self.session = requests.Session()
        self.session.auth = (self.cfg.username, self.cfg.password)

        self.login = LoginEndpoint(self.session, self.cfg)
        self.user = UserEndpoint(self.session, self.cfg)
