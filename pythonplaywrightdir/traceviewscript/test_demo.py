from datetime import time


def test_automsuggestion(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.locator("input[name='username']").fill("Admin")
        page.locator("input[name='password']").fill("admin123")
        page.locator("button[type='submit']").click()
        page.wait_for_timeout(5000)
        page.close()
    finally:
        browser.close()