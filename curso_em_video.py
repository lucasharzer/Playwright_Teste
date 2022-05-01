from playwright.sync_api import sync_playwright
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())
url = str(os.getenv("URL"))
pesquisa = str(os.getenv("PESQUISA_CEV"))

try:
    with sync_playwright() as p:

        # Abrir o navegador
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
                break
            except:
                pass

        page.click("span[class='menu-item-text']")
        
        while True:
            try:
                page.title()
                break
            except:
                pass

        msg = page.inner_text("div[class='entry-content']")
        page.wait_for_timeout(3000)

        print(f"\n-> {msg}")

        browser.close()

except KeyboardInterrupt:
    print("\nProcesso foi interrompido pelo usuário.")
finally:
    print("\nProcesso finalizado com sucesso.")