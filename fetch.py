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
driver = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32 (2)\chromedriver.exe', chrome_options=options)
# driver.maximize_window()
options.add_argument(r"--user-data-dir=C:\Users\PC\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r'--profile-directory=Profile 2') #e.g. Profile 3
options.add_experimental_option("detach", True)



def openwebsite(website):
    driver.get(website)

def clickcookie():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div[2]/div/div[1]/div/div[2]/div/button[2]"))).click()
def load():
    element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]")
    driver.execute_script("arguments[0].scrollIntoView(true);", element);
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]"))).click()

def geniusfetch():
    openwebsite("https://genius.com/Jay-z-holy-grail-lyrics")
    print(driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div/div/div[2]").text)

def azfetch():
    openwebsite("https://www.azlyrics.com/lyrics/oliviarodrigo/vampire.html")
    print(driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]").text)

    
