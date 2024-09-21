import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re
import sys

edge_driver_path = 'C:\\Users\\Linzz\\Desktop\\edgedriver_win64\\msedgedriver.exe'

edge_options = EdgeOptions()
edge_service = EdgeService(executable_path=edge_driver_path)
driver = webdriver.Edge(service=edge_service, options=edge_options)

driver.get("https://authenticate.riotgames.com/")
time.sleep(2)

search_box_Username = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/div/div/div[1]/div[2]/div/input')
search_box_Username.send_keys('batida89')
time.sleep(1)

if search_box_Username.get_attribute("value") == 'batida89':
    print("O usuario foi inserido corretamente")
else:
    print("O usuario não foi inserido corretamente")
    sys.exit()

search_box_Password = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/div/div/div[1]/div[3]/div/input')
search_box_Password.send_keys('rosa3935')
if search_box_Password.get_attribute("Value") == 'rosa3935':
    print("A senha foi inserida corretamente")
else:
    print("A senha não foi inserida corretamente")

finalizarRegistro = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/form/div/div/div[2]/button')
finalizarRegistro.click()
time.sleep(1)



