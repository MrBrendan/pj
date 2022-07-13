from fake_useragent import UserAgent
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import psycopg2
from config import host,user,password,db_name
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def page():
    global driver
    try:
        driver.quit()
    except:
        pass
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}') #смена юзер агентов
    print(userAgent)
    driver = Chrome(executable_path=r"C:\Users\pirat\Desktop\111\chromedriver.exe", options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    driver.set_page_load_timeout(30)
def driv():
    return driver
def start():
    global options
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1280,1024") #полный экран окна
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument('--disable-extensions')
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) #исключаем коллекцию переключателей
    options.add_experimental_option('useAutomationExtension', False) #выключаем useAutomationExtension
    options.add_argument('--disable-blink-features=AutomationControlled') #если не открывает второй запрос
    options.add_argument("--disable-blink-features")
    #driver.execute_script("Object.defineProperty(navigator, 'deviceMemory', {get: () => Number(6)})") #изменяем свойство deviceMemory
    #driver.execute_script("Object.defineProperty(navigator, 'hardwareConcurrency', {get: () => 8})") #изменяем свойство hardwareConc
    #driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})") #изменяем свойство plugins
    try:
        global connection
        connection = psycopg2.connect(  # подключаемся к базе (объект класса pymysql с методом connect)
            host=host,
            user=user,
            password=password,
            database=db_name,
        )
        print('Successfully connected database')
    except Exception as ex:
        print("Connection refused by ")
        print(ex)
def prs():
    global driver
    sh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    reg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.b-header__location-chooser")))
    pages = driver.find_elements(By.XPATH, "//div[@class = 'b-pagination__pages']//a/div[@class = 'b-button__content']")
    for page in pages:
        print(page.text)
    def body():
        product_names = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'b-offer__description')))
        prices = driver.find_elements(By.CLASS_NAME,"b-offer__price-new")
        sales = driver.find_elements(By.CLASS_NAME,"b-offer__badge")
        dates = driver.find_elements(By.CLASS_NAME,"b-offer__dates")
        with connection.cursor() as cursor:
            for n in range(0,len(product_names)-1):
                insert_script = "INSERT INTO alll (product, price, sale, date, shop, region) VALUES (%s,%s,%s,%s,%s,%s)"
                s = (product_names[n].text, prices[n].text, sales[n].text, dates[n].text, reg.text, sh.text)
                cursor.execute(insert_script, s)
                if n==len(product_names)-1:
                    continue
                else:
                    print('Loaded '+(str(n))+" of "+str(len(product_names)-1)+' goods', end="\r") #процесс парсинга с возвратом каретки
    body()
    #driver.current_url
def pokazhi():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM alll')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    connection.close()
    print('Closed connection database')
