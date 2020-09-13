# Import deps
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome webdriver SSL disabling options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# options.add_argument("user-data-dir=./chrome/userdata") 
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# Browser variable setting the browser driver and utilising options as above
browser = webdriver.Chrome(executable_path='./chrome/chromedriver',options=options)

browser.get('chrome://settings/resetProfileSettings?origin=userclick&search=reset')