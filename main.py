from fastapi import FastAPI
from playwright.async_api import async_playwright

app = FastAPI()


@app.get("/")
async def home():
    return {
        "success": True,
        "message": "LeetCode API is running"
    }


@app.get("/leetcode")
async def get_leetcode_profile():
    url = "https://leetcode.com/u/nidhi_123-4/"

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        try:
            await page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=30000
            )

            title = await page.title()

            print("Title:", title)

            return {
                "success": True,
                "title": title
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

        finally:
            await browser.close()
