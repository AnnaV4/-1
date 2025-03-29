import re
from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
# Stop tracing and export it into a zip archive.
    
    
    page = context.new_page()
    page.goto("https://ubiquitous-train-9gxjr557wwxfpqg6-8000.app.github.dev/admin/login/?next=/admin/")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("admin")
    page.get_by_role("textbox", name="Username:").press("Enter")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("123987")
    page.goto("https://ubiquitous-train-9gxjr557wwxfpqg6-8000.app.github.dev/nocodb_data")
    # ---------------------

    context.tracing.stop(path = "playwright/trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)