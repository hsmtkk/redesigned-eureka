import os
import dotenv
from playwright.sync_api import Playwright, sync_playwright, expect

dotenv.load_dotenv()

TNEWS_USERNAME = os.environ["TNEWS_USERNAME"]
TNEWS_PASSWORD = os.environ["TNEWS_PASSWORD"]


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tnews.jp/login?p_ghead")
    page.get_by_role("textbox", name="メインメールアドレスを入力してください").click()
    page.get_by_role("textbox", name="メインメールアドレスを入力してください").fill(
        TNEWS_USERNAME
    )
    page.get_by_role("textbox", name="パスワードを入力してください").click()
    page.get_by_role("textbox", name="パスワードを入力してください").fill(
        TNEWS_PASSWORD
    )
    page.get_by_role("button", name="ログイン").click()
    page.wait_for_load_state("networkidle")
    page.screenshot(path="screenshot.png")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
