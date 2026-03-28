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
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    #maximise the browser window
    context =browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    time.sleep(5)
    browser.close()

#
def test_basicApplicationFunction(playwright):
    print("This is first launch browser test")
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #return the title of the page
    title= page.title()
    print("The title of the page is: ", title)
    #get page url
    appurl= page.url
    print("The url of the page is: ", appurl)
    #get the page DOM content
    domcontent = page.content()
    #print("The content of the page is: ", domcontent)
    isPresent= "my-password" in domcontent
    print("Is the password field present in the page: ", isPresent)
    time.sleep(2)
    browser.close()

def test_browserNavigationCommands(playwright):
    print("This is first launch browser test")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    print("The title of the page is: ", page.title())
    page.goto("https://jqueryui.com/droppable/")
    print("The title of the page is: ", page.title())
    #go back to the previous page
    page.go_back()
    print("The title of the page is after going back : ", page.title())
    #go forward to the next page
    page.go_forward()
    print("The title of the page is after going forward : ", page.title())
    #refresh the page
    page.reload()
    print("The title of the page is after refreshing : ", page.title())
    time.sleep(2)
    browser.close()


def test_sendData(playwright):
    print("This function will send data to the input field")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #return the element
    inputtext= page.locator("#my-text-id")
    #check if input field is enabled
    isEnabled = inputtext.is_enabled()
    print("Is the input field enabled: ", isEnabled)

    #check if the input field is visible
    isVisible = inputtext.is_visible()
    print("Is the input field visible: ", isVisible)

    #inputtext= page.get_by_test_id("my-text-id")
    inputtext.fill("This is a test for sending data to the input field")
   # page.fill("#my-text-id", "This is a test for sending data to the input field")

    dummyfield= page.locator("[name='my-disabled']")
    #check if the dummy field is enabled
    isEnabled = dummyfield.is_enabled()
    print("Is the dummy field enabled: ", isEnabled)

    #check if the dummy field is visible
    isVisible = dummyfield.is_visible()
    print("Is the dummy field visible: ", isVisible)
    time.sleep(2)
    browser.close()

def test_handleCheckBoxAndRadioButton(playwright):
    print("This function will send data to the input field")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #select second checkbox
    checkbox2 = page.locator("#my-check-2")
    print("Is the checkbox2 selected: ", checkbox2.is_checked())
    checkbox2.check()
    print("Is the checkbox2 selected: ", checkbox2.is_checked())
    checkbox1 = page.locator("#my-check-1")
    print("Is the checkbox1 selected: ", checkbox1.is_checked())
    checkbox1.uncheck()
    print("Is the checkbox1 selected: ", checkbox1.is_checked())
    time.sleep(2)
    #radio button
    radiobutton = page.locator('#my-radio-2')
    #check() method will check the radio button if it is not already checked
    radiobutton.click()
    print("is radio button checked", radiobutton.is_checked())
    #click on button
    submitbtn=page.locator("[type='submit']")
    submitbtn.click()
    time.sleep(2)
    #fetching the text from the element
    message= page.locator(".display-6")
    print(message.text_content())
    time.sleep(2)
    browser.close()


def test_handleDropdownUsingSelect_option(playwright):
    print("This function will handle the dropdown")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #select option from dropdown
    #page.select_option("#my-select", "2")
    page.select_option("select", label="Two")
    time.sleep(2)
    page.select_option("select", value="3")
    time.sleep(2)
    page.select_option("select", index="1")
    time.sleep(2)
    browser.close()

def test_handleDropdownUsingSelect_option2(playwright):
    print("This function will handle the dropdown")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #fetch all available options from the dropdown
    allcontent = page.locator("[name='my-select']").all()
    print("All the options available in the dropdown are: ")
    for option in allcontent:
        print(option.text_content())
     #fetch the default selected option from the dropdown
    selectdropdown=page.locator("[name='my-select']")
    default_selected=selectdropdown.input_value()
    print("The default selected option from the dropdown is: ", default_selected)
    #select option from dropdown
    #page.select_option("#my-select", "2")
    # selectdropdown=page.locator("[name='my-select']")
    text_input = page.locator("//input[@id='my-text-id']")
    text_input.clear()
    text_input.fill("This is a test for sending data to the input field")
    selectdropdown.select_option(label="Two")
    browser.close()


def test_handleFrame(playwright):
    print("This function will handle the dropdown")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://jqueryui.com/droppable/")
    #switch to the frame
    frame= page.frame_locator(".demo-frame")
    drag1= frame.locator("#draggable")
    print("Is the drag element visible: ", drag1.is_visible())
    browser.close()

def test_dragAndDrop(playwright):
     print("This function will handle the dropdown")
     browser = playwright.chromium.launch(headless=False)
     # maximise the browser window
     context = browser.new_context()
     page = context.new_page()
     page.goto("https://jqueryui.com/droppable/")
     # switch to the frame
     frame = page.frame_locator(".demo-frame")
     source= frame.locator("#draggable")
     target = frame.locator("#droppable")
     time.sleep(5)
     source.drag_to(target)
     time.sleep(5)
     browser.close()

def test_handleAlerts(playwright):
    print("This function will handle the alerts")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")
    def on_dialog(dialog):
        print("Dialog message: ", dialog.message)
        dialog.accept()
    page.on("dialog", on_dialog)
    time.sleep(5)
    page.locator("#my-alert").click()
    time.sleep(5)
    browser.close()

def test_handleConfirmationAlert(playwright):
    print("This function will handle the confirmation alerts")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")
    def on_dialog(dialog):
        print("Dialog message: ", dialog.message)
        dialog.dismiss() #dismiss() method will click on the cancel button of the confirmation alert
    page.on("dialog", on_dialog)
    page.locator("#my-confirm").click()
    confirmtext = page.locator("#confirm-text")
    print("After handling the confirm alert ", confirmtext.text_content())
    browser.close()


def test_handlePromptAlert(playwright):
    print("This function will handle the prompt alerts")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/dialog-boxes.html")
    def on_dialog(dialog):
        print("Dialog message: ", dialog.message)
        dialog.accept("My name is Test Java") #accept() method will click on the ok button of the prompt alert and send the text to the input field of the prompt alert
    page.on("dialog", on_dialog)
    page.locator("#my-prompt").click()
    #page.evaluate("prompt('Enter your name:', 'default')") #this will trigger the prompt alert
    prompttext = page.locator("#prompt-text")
    print("After handling the prompt alert ", prompttext.text_content())
    browser.close()

def test_handleCalender(playwright):
    print("This function will handle the calender")
    browser = playwright.chromium.launch(headless=False)
    # maximise the browser window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    # sending data to calender uaing fill() method
    # tag should be input
    # page.locator("#my-date").fill("2024-06-30")
    # time.sleep(5)
    # browser.close()
    calender= page.locator("input[name='my-date']")
    calender.click()
    caltext= page.locator("//div[@class='datepicker-days']/table/thead/tr[2]/th[2]").inner_text()
    print("The month and year displayed in the calender is: ", caltext)
    month, year= caltext.split()
    print(f"Month: {month}, Year: {year}")
    print(type(year))
    nextYear = int(year) + 1
    print("Next Year: ", nextYear)
    while True:
        if month == "June" and year == str(nextYear):
            break
        page.locator("//div[@class='datepicker-days']/table/thead/tr[2]/th[3]").click()
        caltext = page.locator("//div[@class='datepicker-days']/table/thead/tr[2]/th[2]").text_content()
        month, year = caltext.split()

    page.locator("//td[normalize-space()='17']").click()
    time.sleep(5)
    page.locator("//h1").click()
    browser.close()

