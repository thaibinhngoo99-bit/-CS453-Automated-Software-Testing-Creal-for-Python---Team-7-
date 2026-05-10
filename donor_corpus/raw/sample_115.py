import pytest
from pages.aplication import Application


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--base_url', action='store', default='https://prodoctorov.ru/new/rate/doctor/12/'
                     , help="Choose base_url")


@pytest.fixture
def app(request):
    browser_name = request.config.getoption("--browser_name")  # для вызова из командной строки и выбора браузера
    base_url = request.config.getoption("--base_url")
    fixture = Application(browser_name=browser_name, base_url=base_url)
    yield fixture
    print("\nquit browser..")
    fixture.destroy()
    return fixture

