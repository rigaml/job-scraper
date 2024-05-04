import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

def find_element_or_none(doc: webdriver.Chrome, selector: str) -> str:
    """
    Finds an element in the Html document and returns its text.
    
    Args:
        doc: section of the document where going to search for the selector.
        selector: CSS selector targeting element to be selected.
    
    Returns:
        The text associated to the selector.
    """    
    try:
        return doc.find_element(By.CSS_SELECTOR, selector).text
    except (NoSuchElementException):
        return None
    except (StaleElementReferenceException):
        time.sleep(1)
        return doc.find_element(By.CSS_SELECTOR, selector).text

