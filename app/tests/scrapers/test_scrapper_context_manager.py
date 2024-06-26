import pytest
from unittest.mock import patch
from app.scrapers.scrapper_context_manager import ScrapperContextManager  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_webdriver():
    with patch('app.scrapers.scrapper_context_manager.webdriver') as mock:
        yield mock

@pytest.fixture
def mock_options():
    with patch('app.scrapers.scrapper_context_manager.Options') as mock:
        yield mock

@pytest.fixture
def mock_service():
    with patch('app.scrapers.scrapper_context_manager.Service') as mock:
        yield mock

@pytest.fixture
def mock_chrome_driver_manager():
    with patch('app.scrapers.scrapper_context_manager.ChromeDriverManager') as mock:
        yield mock

def test_scrapper_context_manager_init(mock_webdriver, mock_options, mock_service, mock_chrome_driver_manager):
    url = "https://example.com"
    show_browser = False

    context_manager = ScrapperContextManager(url, show_browser)

    assert context_manager.url == url
    assert context_manager.show_browser == show_browser
    assert not hasattr(context_manager, 'driver')

def test_scrapper_context_manager_enter_calling_correct_paramters(mock_webdriver, mock_options, mock_service, mock_chrome_driver_manager):
    url = "https://example.com"
    show_browser = False

    context_manager = ScrapperContextManager(url, show_browser)

    mock_options_instance = mock_options.return_value
    mock_service_instance = mock_service.return_value
    mock_driver = mock_webdriver.Chrome.return_value

    with context_manager as cm:
        assert cm == context_manager
        assert context_manager.driver == mock_driver

        # Assert that options were set correctly
        mock_options_instance.add_argument.assert_any_call("--headless")
        mock_options_instance.add_argument.assert_any_call("--enable-javascript")
        mock_options_instance.add_argument.assert_any_call("--window-size=2560,1440")

        # Assert that Chrome was initialized correctly
        mock_webdriver.Chrome.assert_called_once_with(service=mock_service_instance, options=mock_options_instance)

        # Assert that the driver navigated to the correct URL
        mock_driver.get.assert_called_once_with(url)

def test_scrapper_context_manager_exit(mock_webdriver, mock_options, mock_service, mock_chrome_driver_manager):
    url = "https://example.com"
    show_browser = False

    context_manager = ScrapperContextManager(url, show_browser)

    mock_driver = mock_webdriver.Chrome.return_value

    with context_manager:
        # creates the context for later verification
        pass

    # Assert that driver.quit() was called
    mock_driver.quit.assert_called_once()

def test_scrapper_context_manager_show_browser(mock_webdriver, mock_options, mock_service, mock_chrome_driver_manager):
    url = "https://example.com"
    show_browser = True

    context_manager = ScrapperContextManager(url, show_browser)

    mock_options_instance = mock_options.return_value

    with context_manager:
        # Assert that --headless option was not added
        assert not any("--headless" in call[0][0] for call in mock_options_instance.add_argument.call_args_list)