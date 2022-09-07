import pytest
from selenium import webdriver
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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
        
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = ser)# , options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path=IEDriverManager().install())

    elif browser_name == "Edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())

    elif browser_name == "mobile":
        driver = mobile_emulation = { "deviceName": "iPhone XR" }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = driver = webdriver.Chrome(ChromeDriverManager().install(),
        desired_capabilities = chrome_options.to_capabilities())

    elif browser_name == "real_device":
        WIDTH = 320
        HEIGHT = 640
        PIXEL_RATIO = 3.0 # Pixel ratio
        UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
        driver = mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
        driver = driver = webdriver.Chrome(ChromeDriverManager().install(),
        desired_capabilities = chrome_options.to_capabilities())
       
    driver.maximize_window()
    driver.get("https://user:pass@staging-hz.collegedekho.com/?magicflag=1")
    request.cls.driver = driver
    yield
    driver.close()
    

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])

#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra


# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)

