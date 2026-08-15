from fastapi import FastAPI, HTTPException, Query
from playwright.async_api import async_playwright

app = FastAPI()

@app.get("/title")
async def get_title(url: str = Query(..., description="URL to fetch title from")):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url, wait_until="networkidle", timeout=30000)
            title = await page.title()
            await browser.close()
        return {"url": url, "title": title}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
