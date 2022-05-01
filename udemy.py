from playwright.sync_api import sync_playwright
from dotenv import load_dotenv, find_dotenv
import os
from time import sleep


load_dotenv(find_dotenv())
url = str(os.getenv("URL"))
pesquisa = str(os.getenv("PESQUISA_U_1"))
busca = str(os.getenv("PESQUISA_U_2"))

try:
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        while True:
            try:
                page.title()
                break
            except:
                pass
        
        page.fill("input[name='q']", pesquisa)
        page.click("input[class='gNO89b']")

        while True:
            try:
                page.click("h3[class='LC20lb MBeuO DKV0Md']")
                page.wait_for_timeout(2000)
                break
            except:
                pass
        
        page.fill("input[name='q']", busca)
        page.wait_for_timeout(2000)

        browser.close()
except KeyboardInterrupt:
    print("\nProcesso finalizado.")
