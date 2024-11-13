from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
import os
from datetime import datetime
import sys

# Get the absolute path of the project root directory (AVOLTA_TESTS)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)


@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')

    timestamp = datetime.now().strftime("%m_%d_%H_%M")
    report_file = os.path.join('reports', f'report_{timestamp}.html')

    config.option.htmlpath = report_file
    config.option.self_contained_html = True
