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
    page.goto("https://finviz.com/login.ashx")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(FINVIZ_USERNAME)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(FINVIZ_PASSWORD)
    page.get_by_role("button", name="Log in").click()

    # do not work due to an advertizement
    # page.wait_for_load_state("networkidle")

    time.sleep(5)
    page.screenshot(path="screenshot.png")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
