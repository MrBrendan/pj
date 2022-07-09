import functions


from numpy.random import default_rng

functions.start()
functions.page()
try:
    functions.driv().get('https://bot.sannysoft.com/')
    print('Connected site')
except Exception as ex:
    print("Connection refused by ")
    print(ex)
#functions.prs()
#functions.pokazhi()
#category