import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_text("Username", exact=True)).to_be_visible()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    expect(page.locator("form")).to_contain_text("Password")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Admin").click()
    page.get_by_role("button", name=" Add").click()
    page.get_by_role("textbox", name="Type for hints...").click()
    page.get_by_role("textbox", name="Type for hints...").fill("User1")
    page.get_by_text("-- Select --").first.click()
    page.get_by_role("option", name="ESS").click()
    page.get_by_text("-- Select --").click()
    page.get_by_role("option", name="Enabled").click()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("user1")
