import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


def find_element_text(doc: WebElement, selector: str) -> str:
    """
    Finds an element in the Html document and returns its text.

    Args:
        doc: section of the document where going to search for the selector.
        selector: CSS selector targeting element to be selected.

    Returns:
        The text associated to the selector or empty if no selector is found.
    """
    try:
        return doc.find_element(By.CSS_SELECTOR, selector).text
    except (NoSuchElementException):
        return ""
    except (StaleElementReferenceException):
        time.sleep(1)
        return doc.find_element(By.CSS_SELECTOR, selector).text
