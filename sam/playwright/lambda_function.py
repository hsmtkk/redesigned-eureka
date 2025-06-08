import json
from playwright.sync_api import Playwright, sync_playwright


def handler(event, context):
    main()
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "ok",
            }
        ),
    }


def run(playwright: Playwright) -> None:
    args = ["--single-process"]
    browser = playwright.chromium.launch(headless=True, args=args)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.example.com/")
    page.get_by_role("link", name="More information...").click()
    page.wait_for_load_state("networkidle")
    print(page.content())
    page.screenshot(path="/tmp/screenshot.png")
    context.close()
    browser.close()


def main():
    print("begin")
    with sync_playwright() as playwright:
        run(playwright)
    print("end")
