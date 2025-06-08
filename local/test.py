import os
import time
import dotenv
from playwright.sync_api import Playwright, sync_playwright, expect

dotenv.load_dotenv()
FINVIZ_USERNAME = os.environ["FINVIZ_USERNAME"]
FINVIZ_PASSWORD = os.environ["FINVIZ_PASSWORD"]


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.example.com/")
    page.get_by_role("link", name="More information...").click()
    page.wait_for_load_state("networkidle")
    print(page.content())
    page.screenshot(path="screenshot.png")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
