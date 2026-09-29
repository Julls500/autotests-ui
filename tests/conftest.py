import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
     browser = playwright.firefox.launch(headless=False)
     yield browser.new_page()
     browser.close()

'''
@pytest.fixture
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        yield browser.new_page()
        browser.close()
'''