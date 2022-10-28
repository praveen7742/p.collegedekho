import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.common.by import By

# @pytest.fixture()

# def setup():
#     driver = webdriver.Chrome()
#     return driver


driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        
        

        driver = webdriver.Chrome(ChromeDriverManager().install()) #,options=chrome_options)
        # ser = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service = ser)#,options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    elif browser_name == "IE":
        driver = webdriver.Ie(service=Service(IEDriverManager().install()))

    elif browser_name == "Edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())

    elif browser_name == "mobile":
        driver = mobile_emulation = { "deviceName": "iPhone X" }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = Service(ChromeDriverManager().install())
        desired_capabilities = chrome_options.to_capabilities()

    driver.maximize_window()
    return driver
    
   
        

    
    




    
