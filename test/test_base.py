import os

import pytest
from utilities.logger import get_logger

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request,driver,config):
        request.cls.driver = driver
        request.cls.config = config["environment"]["CRM"]
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info("CRM TEST HAS STARTED")
        yield
        self.logger.info("CRM TEST HAS FINISHED")
