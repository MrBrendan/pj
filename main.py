try:
    from selenium.webdriver import Chrome
    driver.quit()
except:
    pass
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
options = ChromeOptions()
#options.add_argument("--headless")
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
def connect_db():
    import psycopg2
    from cnf import host, user, password, db_name
    try:
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
connect_db()
from cnf import path_driver
s=Service(path_driver)
driver = Chrome(service=s, options=options)
from fake_useragent import UserAgent
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')  # смена юзер агентов
print(userAgent)
from selenium_stealth import stealth
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
driver.set_page_load_timeout(30)
try:
    from cnf import url
    driver.get(url)
    print('Connected site')
except Exception as ex:
    print("Connection refused by ")
    print(ex)
from functions import prs