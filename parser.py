import functions,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from numpy.random import default_rng

functions.start()
functions.page()
try:
    functions.driv().get('https://edadeal.ru/')
    print('Connected site')
except Exception as ex:
    print("Connection refused by ")
    print(ex)
WebDriverWait(functions.driv(), 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Изменить')]"))).click()
regions = functions.driv().find_elements(By.CLASS_NAME,"b-root__location-name")
for region in regions:
    print(str(region.text), end = '\n')
x=str(input("=======>Укажите регион: "))
#functions.driv().find_elements(By.CLASS_NAME,"b-root__location-name")

WebDriverWait(functions.driv(), 60).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '" + x + "')]"))).click()
time.sleep(1)
functions.driv().find_element(By.XPATH, "//*[contains(text(), 'Магазины')]").click()
#obj=str(input("Что: "))


#//td[text()='UserID']
#main_page = functions.driv().page_source
#fileToWrite = open(r"C:\Users\pirat\Desktop\111\page_source.html", "w", encoding='utf-8')
#fileToWrite.write(main_page)
#fileToWrite.close()
#functions.prs()
#functions.pokazhi()
#category