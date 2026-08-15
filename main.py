@app.get("/leetcode")
async def get_leetcode_profile():
    url = "https://leetcode.com/u/nidhi_123-4/"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(url, wait_until="domcontentloaded")

        username = await page.locator("h1").first.inner_text()

        await browser.close()

    return {
        "username": username
    }
