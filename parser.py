try:
    from main import driver
    from main import url
    driver.get(url)
    print('Connected site')
except Exception as ex:
    print("Connection refused by ")
    print(ex)

#main_page = functions.driv().page_source
#fileToWrite = open(r"C:\Users\pirat\Desktop\111\page_source.html", "w", encoding='utf-8')
#fileToWrite.write(main_page)
#fileToWrite.close()
#functions.prs()
#functions.pokazhi()
#category