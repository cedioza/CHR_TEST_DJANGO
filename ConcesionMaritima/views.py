from django.http import HttpResponse
from django.shortcuts import render

# Selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json

from ConcesionMaritima.models import DatosConcesion


def bot(request):
    options = Options()
    # options.headless = True
    # # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--incognito")

    driver_path = "./drivers/chromedriver.exe"
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.concesionesmaritimas.cl/")

    time.sleep(5)
    driver.switch_to.frame("centro_sigmar")
    elemento_iframe = driver.find_element(
        By.XPATH, "//td[@bgcolor='#f3fbff']/iframe")
    driver.switch_to.frame(elemento_iframe)

    # Esperar a que la página cargue completamente
    # Esperar hasta 10 segundos (puede ajustarse según sea necesario
    driver.implicitly_wait(10)
    # antes = driver.find_elements(By.XPATH, '//a[contains(@class, "manhattan--container")]')
    select_element = driver.find_element(
        By.XPATH, '//select[contains(@name, "Region")]')
    select = Select(select_element)
    select.select_by_value("2")

    select_element = driver.find_element(
        By.XPATH, '//select[contains(@name, "variableGobmar")]')

    select = Select(select_element)
    select.select_by_value("12")

    select_element = driver.find_element(
        By.XPATH, '//select[contains(@name, "variableCapuerto")]')
    select = Select(select_element)
    select.select_by_value("13")
    time.sleep(5)
    boton = driver.find_element(By.XPATH, '//img[@name="verlistado"]')
    # Hacer clic en el botón
    boton.click()
    wait = WebDriverWait(driver, 10)
    elementos = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, '//table[@width="800"]')))

    # Obtener los elementos de la tabla
    tabla = driver.find_element(By.XPATH, "//table[@border='1']//tbody")
    filas = tabla.find_elements(By.XPATH, ".//tr")

    datos = []

    for fila in filas:
        columnas = fila.find_elements(By.XPATH, ".//td")
        fila_datos = [columna.text for columna in columnas]
        datos.append(fila_datos)

    with open('datos.json', 'w') as archivo:
        json.dump(datos, archivo)   

    for fila_datos in datos:
        concesion = DatosConcesion(
            concesion=fila_datos[0],    
            tipo_concesion=fila_datos[1],
            comuna=fila_datos[2],   
            lugar=fila_datos[3],    
            rs_ds=fila_datos[4],    
            tipo_tramite=fila_datos[5],
            concesionario=fila_datos[6],
            tipo_vigencia=fila_datos[7]
        )
    concesion.save()
 
    driver.quit()

    return HttpResponse("Datos guardados correctamente")
