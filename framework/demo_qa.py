from hosts_config import Hosts
from utils.base_session import BaseSession


class DemoQaWithEnv:
    def __init__(self, env):
        self.demo_web_shop = BaseSession(url=Hosts(env).demo_web_shop)
        self.reqres = BaseSession(url=Hosts(env).reqres)
        self._authorization_cookie = None

    def login(self, email, password):
        return self.demo_web_shop.post(
            url="/login",
            params={'Email': email, 'Password': password},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )

    @property
    def authorization_cookie(self):
        return self._authorization_cookie

    @authorization_cookie.setter
    def authorization_cookie(self, response):
        self._authorization_cookie = {"NOPCOMMERCE.AUTH": response.cookies.get("NOPCOMMERCE.AUTH")}
