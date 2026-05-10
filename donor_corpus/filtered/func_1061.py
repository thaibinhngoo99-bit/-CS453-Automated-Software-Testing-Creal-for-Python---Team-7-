@pytest.fixture
def app(request):
    browser_name = request.config.getoption('--browser_name')
    base_url = request.config.getoption('--base_url')
    fixture = Application(browser_name=browser_name, base_url=base_url)
    yield fixture
    print('\nquit browser..')
    fixture.destroy()
    return fixture