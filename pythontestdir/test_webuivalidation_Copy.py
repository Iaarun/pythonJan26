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

def test_handle_alerts(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")
    # register handler before triggering any dialogs
    def on_dialog(dialog):
        print("Alert Text:", dialog.message)
        dialog.accept()
    page.on("dialog", on_dialog)
    # trigger dialogs (the handler will run and accept them)
    page.locator("#my-alert").click()
    page.evaluate("alert('This is an alert!')")
    page.wait_for_timeout(2000)
    browser.close()

# python
def test_handle_confirmation(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")
    def on_dialog(dialog):
        print("Dialog type:", dialog.type, "Message:", dialog.message)
        if dialog.type == "confirm":
            dialog.accept()  # use dialog.dismiss() to cancel instead
    page.on("dialog", on_dialog)
    # trigger confirm dialog (button on the page and an inline confirm)
    page.locator("#my-confirm").click()
    #evalute is used to execute JavaScript code in the context of the page.
    # Here, it triggers a confirm dialog with the message 'Do you confirm?'
    page.evaluate("confirm('Do you confirm?')")
    page.wait_for_timeout(1500)
    browser.close()


def test_handle_prompt(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")

    def on_dialog(dialog):
        print("Dialog type:", dialog.type, "Message:", dialog.message)
        if dialog.type == "prompt":
            dialog.accept("Automated response")  # send text; use dialog.dismiss() to cancel
    page.on("dialog", on_dialog)
    # trigger prompt dialog (button on the page and an inline prompt)
    page.locator("#my-prompt").click()
    page.evaluate("prompt('Enter your name:','default')")
    page.wait_for_timeout(1500)
    browser.close()


from pathlib import Path

def test_download_pdf(playwright):
    downloads_dir = Path.cwd() / "downloads"
    downloads_dir.mkdir(parents=True, exist_ok=True)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("https://letcode.in/file")
    # Wait for the download triggered by clicking the first PDF link on the page
    with page.expect_download() as download_info:
        page.locator('a[href$=".pdf"]').first.click()
    download = download_info.value
    filename = download.suggested_filename
    dest = downloads_dir / filename
    download.save_as(str(dest))

    print("Saved download to:", dest)
    assert dest.exists()
    browser.close()


from pathlib import Path

def test_upload_sample_pdf(playwright):
    downloads_dir = Path.cwd() / "downloads"
    file_path = downloads_dir / "sample.pdf"
    assert file_path.exists(), f"File not found: {file_path}"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Change the URL below to the page that contains the file input you want to test
    page.goto("https://letcode.in/file")
    # Locate the file input and upload the file
    # Adjust the selector if the page uses a different input locator
    file_input = page.locator('input[type="file"]')
    file_input.set_input_files(str(file_path))
    # Optional: if the page requires a submit/upload button, click it
    # page.locator("button[type='submit']").click()
    page.wait_for_timeout(1500)
    browser.close()

# python
from datetime import date
import time

from playwright.sync_api import sync_playwright

def test_handle_calendar(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    # Click the date field
    page.locator("input[name='my-date']").click()
    caldata = page.locator("//div[@class='datepicker-days']/table/thead/tr[2]/th[2]").inner_text()
    print(caldata)
    month = caldata.split(" ")[0].strip()
    year = caldata.split(" ")[1].strip()
    print(f"Month: {month} Year: {year}")
    nextYear = int(year) + 1
    while True:
        if month == "March" and year == "2027":
            break
        page.locator("//div[@class='datepicker-days']/table/thead/tr[2]/th[3]").click()
        caldata = page.locator("//div[@class='datepicker-days']/table/thead/tr[2]/th[2]").inner_text()
        month, year = caldata.split()
    print("Reached target month and year")
    page.locator("//td[normalize-space()='17']").click()
    page.locator("//h1").click()

    browser.close()

# python
from playwright.sync_api import sync_playwright

# python
def test_read_row_data(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://vinothqaacademy.com/webtable/")
    # Wait until body rows are present
    page.wait_for_selector("table tbody tr", timeout=10000)
    # choose a row index to read (1-based). Change as needed.
    row_index = 3
    rows = page.locator("table tbody tr")
    rows_count = rows.count()
    if row_index < 1 or row_index > rows_count:
        print(f"Requested row {row_index} not found (found {rows_count} rows).")
        browser.close()
        return []
    row_locator = rows.nth(row_index - 1)
    # ensure the row is visible
    row_locator.wait_for(state="visible", timeout=5000)
    # read all cell texts reliably and trim whitespace
    cell_texts = [t.strip() for t in row_locator.locator("td,th").all_text_contents()]

    print(f"\nReading row {row_index}:")
    for txt in cell_texts:
        print(txt)
    browser.close()

# python
def test_read_column_data(playwright):
    """
    Fixed column reader: waits for table rows, reads a 1-based column index,
    prints values (use `pytest -s` to see output) and returns the list.
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://vinothqaacademy.com/webtable/")
    # Wait for the table body rows to appear
    page.wait_for_selector("table tbody tr", timeout=10000)
    # choose a column index to read (1-based). Change as needed.
    col_index = 2
    column_locator = page.locator(f"table tbody tr td:nth-child({col_index})")
    # Wait for at least one cell to be visible
    column_locator.first.wait_for(state="visible", timeout=5000)
    # Use all_text_contents to fetch all cell texts reliably
    column_values = [txt.strip() for txt in column_locator.all_text_contents()]
    print(f"\nReading column {col_index}:")
    for v in column_values:
        print(v)
    browser.close()

# python
def test_read_complete_table(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://vinothqaacademy.com/webtable/")

    # wait for rows to appear
    page.wait_for_selector("table tbody tr", timeout=10000)

    table = page.locator("table").first

    # read headers (use thead if present, otherwise generate names from first row)
    thead = table.locator("thead tr th")
    headers = []
    if thead.count() > 0:
        headers = [h.strip() for h in thead.all_text_contents()]
    else:
        first_row = table.locator("tbody tr").first
        cols = first_row.locator("td,th").count()
        headers = [f"col_{i+1}" for i in range(cols)]

    # read all body rows using each row's cells' all_text_contents()
    rows_locator = table.locator("tbody tr")
    rows_count = rows_locator.count()
    full_rows = []
    for i in range(rows_count):
        row = rows_locator.nth(i)
        cell_texts = [t.strip() for t in row.locator("td,th").all_text_contents()]
        # if a cell list is empty, try per-cell inner_text() as a fallback (still no evaluate)
        if any(not v for v in cell_texts):
            cells = row.locator("td,th")
            fixed = []
            for j in range(cells.count()):
                txt = cells.nth(j).inner_text().strip() if cells.nth(j).inner_text() else ""
                fixed.append(txt)
            cell_texts = fixed
        full_rows.append(cell_texts)
        print(cell_texts)

    print("Headers:", headers)
    browser.close()
    return {"headers": headers, "rows": full_rows}