#configuration file
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, params=["chrome", "edge"])
def setup_and_teardown(request):
    global driver
    if request.param=="chrome":
        driver = webdriver.Chrome()
    elif request.param=="edge":
        driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()