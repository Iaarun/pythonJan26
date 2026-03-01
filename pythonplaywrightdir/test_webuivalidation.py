import time
from playwright.sync_api import Page

# def test_basicplaywrightfunction(playwright):
#     print("This is first launch browser test")
#     page = playwright.chromium.launch(headless=False)
#     context =page.new_context()
#     page = context.new_page()
#     page.goto("https://bonigarcia.dev/selenium-webdriver-java/dropdown-menu.html")

def test_basicplaywrightfunction(playwright):
    print("This is first launch browser test")
    browser = playwright.chromium.launch(headless=False)
    context =browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/dropdown-menu.html")
    time.sleep(5)
    browser.close()