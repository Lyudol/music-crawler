from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.utils import decode as decode_sw
from seleniumwire.webdriver import ActionChains
import time
from datetime import datetime
import gzip


options = webdriver.ChromeOptions()
sw_options = {
    'disable_encoding': True,  # Ask the server not to compress the response
    'disable_capture': True
}


# options.add_argument(r"--user-data-dir=C:\Users\PC\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument("--disable-infobars")
# options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument('--window-size=1920,1080')
# options.add_argument("--headless")
options.add_experimental_option("detach", True) 


options.add_argument(r'--profile-directory=Profile 1')
driver = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32 (2)\chromedriver.exe', chrome_options=options)
driver.minimize_window()

options.add_argument('--window-size=688,1440')

options.add_argument(r'--profile-directory=Profile 2') 
driverfinder1 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32 (2)\chromedriver.exe', chrome_options=options)
driverfinder1.set_window_position(-862, -1440)


options.add_argument(r'--profile-directory=Profile 3') 
driverfinder2 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32 (2)\chromedriver.exe', chrome_options=options)
driverfinder2.set_window_position(-174, -1440)

options.add_argument(r'--profile-directory=Profile 4') 
driverfinder3 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32 (2)\chromedriver.exe', chrome_options=options)
driverfinder3.set_window_position(514, -1440)

options.add_argument(r'--profile-directory=Profile 5')
driverfinder4 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32 (2)\chromedriver.exe', chrome_options=options)
driverfinder4.set_window_position(1202, -1440)

options.add_argument(r'--profile-directory=Profile 6')
driverfinder5 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32 (2)\chromedriver.exe', chrome_options=options)
driverfinder5.set_window_position(1890, -1440)



def openwebsite(website):
    driver.get(website)
def pagesource(drivertouse):
    return drivertouse.page_source
def openfinderwebsite(website,drivertouse):
    drivertouse.get(website)

def clickcookie(drivertouse):
    WebDriverWait(drivertouse, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div[2]/div/div[1]/div/div[2]/div/button[2]"))).click()
def load(drivertouse):
    element = drivertouse.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]")
    drivertouse.execute_script("arguments[0].scrollIntoView(true);", element);
    WebDriverWait(drivertouse, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]"))).click()

def geniusfetch(website):
    openwebsite(website)
    print(driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]").text)

def azfetch(website):
    openwebsite(website)
    print(driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]").text)

    
