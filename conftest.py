import pytest
import yaml
from pathlib import Path
from playwright.sync_api import sync_playwright
from utils.logger import setup_logger

def load_config(env: str = "dev"):
    config_path = Path(__file__).parent / "config" / f"{env}.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env") if hasattr(request.config, "getoption") else "dev"
    return load_config(env)

@pytest.fixture(scope="function")
def test_logger(request):
    logger = setup_logger(request.node.name)
    logger.info(f"Starting: {request.node.name}")
    yield logger
    logger.info(f"Finished: {request.node.name}")

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment: dev or staging")
