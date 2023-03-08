# Codigo que joga cookie clicker sozinho

# Importando bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Criando a classe com as instruções necessárias
class CookieClicker:
    def __init__(self):
        # Endereço do site
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"

        # Coordenadas dentro do site
        self.SITE_MAP = {
            "buttons": {
                "biscoito" : {
                    "xpath": "/html/body/div/div[2]/div[15]/div[8]/button"
                },
                "upgrade" : {
                    "xpath": "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]" 
                },
                "language" : {
                    "xpath": "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]"
                }
            }
        }

        # Instanciar o driver do selenium para fazer a automatização
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Abre o navegador em tela cheia
        self.driver.maximize_window()

    def abrir_site(self):
        # Abrir o site
        self.driver.get(self.SITE_LINK)

        # Espera o site carregar
        time.sleep(2)

        # Clica na linguagem "English"
        self.driver.find_element("xpath", self.SITE_MAP["buttons"]["language"]["xpath"]).click()
        time.sleep(2)

    def clicar_no_cookie(self):
        # Clica no cookie
        self.driver.find_element("xpath", self.SITE_MAP["buttons"]["biscoito"]["xpath"]).click()

    def pega_melhor_upgrade(self):
        # Achar o upgrade possivel para fazer e jogar melhor
        encontrei = False
        elemento_atual = 2

        while not encontrei:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(elemento_atual))
            classes_objeto = self.driver.find_element("xpath", objeto).get_attribute("class")

            if not "enabled" in classes_objeto:
                encontrei = True
            else:
                elemento_atual += 1
        return elemento_atual - 1
        
    def comprar_upgrade(self):
        # Clica no upgrade 
       
        objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(self.pega_melhor_upgrade()))
        self.driver.find_element("xpath", objeto).click()

# Aplicaçao das instruções da classe para jogar
biscoito = CookieClicker()
biscoito.abrir_site()

i = 0 
while True:
    if i % 500 == 0 and i !=0:
        time.sleep(1)
        biscoito.comprar_upgrade()
        time.sleep(1)
    biscoito.clicar_no_cookie()
    i += 1
