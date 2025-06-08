from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
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


if __name__ == "__main__":
    print("begin")
    with sync_playwright() as playwright:
        run(playwright)
    print("end")
