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

def test_senddata(playwright):
    print("This is first launch browser test")
    browser = playwright.chromium.launch(headless=False)
    context =browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    page.locator("#my-text-id").fill("This is the first test for send data")
    time.sleep(5)
    page.wait_for_selector("#my-check-2", timeout=5000)
    page.locator("#my-check-2").check()
    page.wait_for_selector("#my-check-1", timeout=5000)
    page.locator("#my-check-1").uncheck()
    time.sleep(2)
    browser.close()

def test_selectDropdwonData(playwright):
    print("This is data select from dropn down menu ")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    page.locator("#my-text-id").fill("This is the first test for send data")
    time.sleep(5)
    #select by visible text
    page.select_option("select", label="Two")
    time.sleep(2)
    page.select_option("select", value="3")
    time.sleep(2)
    page.select_option("select", index=1)
    browser.close()

def test_iframehandling(playwright):
    print("This is first test for iframe handling")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://jqueryui.com/droppable/")
    #switch to iframe
    frame = page.frame_locator("iframe.demo-frame")
    source = frame.locator("#draggable")
    target = frame.locator("#droppable")
    source.drag_to(target)
    time.sleep(2)
    browser.close()



from playwright.sync_api import sync_playwright

def test_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open first page
        page.goto("https://example.com")
        print("Title of the first page:", page.title())
        # Navigate to second page
        page.goto("https://www.wikipedia.org")
        print("Title of the second page:", page.title())
        page.go_back()
        print("Title after going back:", page.title())
        page.go_forward()
        print("Title after going forward:", page.title())
        page.reload()
        print("Title after reloading:", page.title())
        page.wait_for_timeout(3000)
        browser.close()

from playwright.sync_api import sync_playwright

def test_page_info():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://example.com")
        # 🌐 Title
        print("Title:", page.title())
        # 🔗 URL
        print("URL:", page.url)

        print("Page Source Length:", len(page.content()))

        print("Page Source:", page.content()[:500])
        # 🧩 Tab Info
        for i, p in enumerate(context.pages):
            print(f"Tab {i} -> {p.url}")

        browser.close()



def test_multiple_tabs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Open first tab
        page1 = context.new_page()
        page1.goto("https://example.com")

        # Open second tab
        page2 = context.new_page()
        page2.goto("https://www.wikipedia.org")

        print("Tab1 Title:", page1.title())
        print("Tab2 Title:", page2.title())
        browser.close()


def test_multiple_tabs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        # First tab
        page = context.new_page()
        page.goto("https://example.com")
        # Open new tab via click (example)
        with context.expect_page() as new_page_info:
            page.evaluate("window.open('https://www.wikipedia.org')")
        #new_page_info.value is the new page that is opened after clicking the link
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        # Work on new tab
        print("New Tab Title:", new_page.title())
        # Switch back to first tab
        page.bring_to_front()
        print("First Tab Title:", page.title())
        browser.close()



