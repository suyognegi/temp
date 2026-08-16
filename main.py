from fastapi import FastAPI
from playwright.async_api import async_playwright

app = FastAPI()


@app.get("/")
async def home():
    return {"status": "running"}


@app.get("/test")
async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()
        await page.goto("https://example.com")

        title = await page.title()

        await browser.close()

        return {"title": title}
