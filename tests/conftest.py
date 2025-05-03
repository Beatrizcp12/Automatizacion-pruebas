import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from helpers.main_po.general_steps_po import MainFunctionPageObject



@pytest.fixture
def main_page():
    driver = MainFunctionPageObject()
    yield driver
    driver.close_web()
