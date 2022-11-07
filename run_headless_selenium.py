from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument("--no-sandbox")
"""Change Download Path"""
# pth = join('')
# pth_out =join(pth,'dump','')
# prefs = {"download.default_directory" : pth_out}
# chrome_options.add_experimental_option("prefs",prefs)
chromedriver = Service(ChromeDriverManager().install())

browser =  webdriver.Chrome(service=chromedriver, options=chrome_options) 
