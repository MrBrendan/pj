import functions,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import url
from numpy.random import default_rng

functions.start()
functions.page()
try:
    functions.driv().get(url)
    print('Connected site')
except Exception as ex:
    print("Connection refused by ")
    print(ex)
print('Список городов:')
WebDriverWait(functions.driv(), 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Изменить')]"))).click()
regions = functions.driv().find_elements(By.CLASS_NAME,"b-root__location-name")
for region in regions:
    print(str(region.text), end = '\n')
x=str(input("===> Укажите регион: "))
#functions.driv().find_elements(By.CLASS_NAME,"b-root__location-name")
WebDriverWait(functions.driv(), 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '" + x + "')]"))).click()
WebDriverWait(functions.driv(), 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Магазины')]"))).click()
shops = WebDriverWait(functions.driv(), 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"b-image__img")))
for shop in shops:
    print(str(shop.get_attribute("alt")), end = '\n')
y=str(input("===> Укажите магазин: "))
WebDriverWait(functions.driv(), 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@alt,'" + y + "')]"))).click()

#main_page = functions.driv().page_source
#fileToWrite = open(r"C:\Users\pirat\Desktop\111\page_source.html", "w", encoding='utf-8')
#fileToWrite.write(main_page)
#fileToWrite.close()
functions.prs()
functions.pokazhi()
#category