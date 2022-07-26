from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')

url = input("Put search url : ")
tname = input("Put keywords file (.txt) : ")
threads = input("threads number : ")
pool = ThreadPoolExecutor(max_workers=int(threads))

try :
    f = open(tname,"r")
except :
    print("file doesn't exist")
    input("Press enter to exit")
    exit()
ks = f.read().splitlines()
def search(line):
    page = 1

    driver = webdriver.Chrome(options=options)
    print(f'searching : {line}')
    driver.get(url)
    sleep(1)
    driver.find_element(By.ID,"q").send_keys(line)
    sleep(1)
    driver.find_element(By.ID,"send_search").submit()
    sleep(2)
    while True :
        print(f'searching {line} page : {str(page)}')
        try :
            driver.find_element(By.CSS_SELECTOR,'[type="submit"][role="link"]').click()
            page += 1
            sleep(1)
        except :
            print(line+' limit reached')
            driver.close()
            break


for line in ks :

    pool.submit(search,line)




