from dataclasses import dataclass
from os import getenv


@dataclass
class Hosts:
    def __init__(self, env):
        self.demo_web_shop = getenv(f'{env.upper()}_DEMOWEBSHOP')
        self.reqres = getenv(f'{env.upper()}_REQRESIN')
