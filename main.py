from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

def wait():
    dots = [".", "..", "...", ".", "..", "..."]
    for i in range(5):
        os.system('clear')
        print("Esperando" + dots[i])
        time.sleep(1)

credentials = {
    'username': "16571560798", 
    'password': "Meuchope@22"
}

def getCredentials():
    if(credentials.length == 0):
        credentials['username'] = input("Digite o usuário para bater o ponto")
        credentials['password'] = input("Digite a senha")

def main():
    print("iniciando script de bater ponto.")

    driver = webdriver.Firefox()
    driver.get("https://app2.pontomais.com.br/registrar-ponto")


    # Coloca as credenciais de usuário
    elem = driver.find_element(By.TAG_NAME, "input")
    elem.send_keys(credentials['username'])

    elem2 = driver.find_element(By.XPATH, "/html/body/app-root/dx-drawer/div/div[2]/div[2]/div/app-container/login/div/div[1]/div/div[4]/div[1]/pm-form/form/div/div/div[2]/pm-input/div/div/pm-text/input")
    elem2.send_keys(credentials['password'])

    # Enter pra fazer login
    elem2.send_keys(Keys.RETURN)

    wait()

    # Entra na tela de bater ponto
    elem = driver.find_element(By.XPATH, "/html/body/app-root/app-side-nav-outer-toolbar/app-header/header/dx-toolbar/div/div[3]/div[2]/dxi-item/pm-button/button")
    elem.click()

    wait()

    # Clica no link de definir a localização fixa
    elem = driver.find_element(By.XPATH, "/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/app-container/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/address-time-card-register/div[2]/p[3]/small")
    elem.click()

    wait()

    elem = driver.find_element(By.XPATH, "/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/app-container/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/div/pm-button/button")
    # elem.click()

    wait()

    # Fecha o navegador
    driver.close()
    print("finalizando script de bater ponto.")

getCredentials()
main()



