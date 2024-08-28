from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def verificar_estrategia(lista):
    for numero in lista[:4]:
        if numero >= 2:
            return False
    return True

# Credenciais embutidas
LOGIN = 'mario@tmpeml.com'
PASSWORD = 'Aviator102030!'

def handler(request):
    options = Options()
    options.add_argument('--disable-logging')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('w3c', True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://estrelabet.com/ptb/games/detail/casino/normal/7787')
    sleep(10)  # Espera para garantir que a página carregue

    print('Acessando aviator...')
    # Adicione mais código aqui para interagir com a página

    # Feche o navegador após o uso
    driver.quit()

    return {
        'statusCode': 200,
        'body': 'Scraping completed.'
    }
