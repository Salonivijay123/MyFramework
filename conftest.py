import os
import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader
import allure
import time

@pytest.fixture(scope="session")
def config():
    return ConfigReader.read_config()

@pytest.fixture(scope="class")
def driver(config):
    environment = "CRM"
    env = config["environment"][environment]
    browser = env["browser"]
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Unsupported browser: {browser}")
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item,call):
        outcome = yield
        rep = outcome.get_result()
        if rep.when == "call" and rep.failed:
            driver = item.funcargs.get("driver", None)
            if driver:
                screenshot_dir = os.path.join("reports", "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)
                file_path = os.path.join(screenshot_dir, f"{item.name}.png")
                driver.save_screenshot(file_path)

                allure.attach.file(file_path, name="screenshot", attachment_type=allure.attachment_type.PNG)



