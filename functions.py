import random
from main import host, user, password, db_name, url
import time

class prs(object):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from main import driver
    print('Список городов:')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Изменить')]"))).click()
    regions = driver.find_elements(By.CLASS_NAME, "b-root__location-name")
    for region in regions:
        print(str(region.text), end='\n')
    x = str(input("===> Укажите регион: "))
    # driver.find_elements(By.CLASS_NAME,"b-root__location-name")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '" + x + "')]"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Магазины')]"))).click()
    shops = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "b-image__img")))
    for shop in shops:
        print(str(shop.get_attribute("alt")), end='\n')
    y = str(input("===> Укажите магазин: "))
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@alt,'" + y + "')]"))).click()
    sh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    reg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.b-header__location-chooser")))
    pages = driver.find_elements(By.XPATH, "//div[@class = 'b-pagination__pages']//a/div[@class = 'b-button__content']")
    product_names = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'b-offer__description')))
    prices = driver.find_elements(By.CLASS_NAME,"b-offer__price-new")
    sales = driver.find_elements(By.CLASS_NAME,"b-offer__badge")
    dates = driver.find_elements(By.CLASS_NAME,"b-offer__dates")
    class conn (prs):
        with connection.cursor() as cursor:
            for n in range(0,len(product_names)-1):
                insert_script = "INSERT INTO alll (product, price, sale, date, shop, region) VALUES (%s,%s,%s,%s,%s,%s)"
                s = (product_names[n].text, prices[n].text, sales[n].text, dates[n].text, reg.text, sh.text)
                cursor.execute(insert_script, s)
                if n==len(product_names)-1:
                    continue
                else:
                    print('Loaded '+(str(n))+" of "+str(len(product_names)-1)+' goods', end="\r") #процесс парсинга с возвратом каретки
            connection.commit()
            time.sleep(1)
class pags(object):  # создаю класс для пересчёта страниц
    pages = prs.pages
    was = [1]
    @classmethod
    def url(cls):
        wasset = set(cls.was)
        pages = [item for item in cls.pages if item not in wasset]
        random.shuffle(pages)  # перемешиваю доступные страницы
        cls.was.append(x)
        url = str('https://edadeal.ru/') + '?page=' + str(x)
        print(url)
        return (url)
def pokazhi():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM alll')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    connection.close()
    print('Closed connection database')
