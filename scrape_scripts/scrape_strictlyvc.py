# Import deps
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import json


# Chrome webdriver SSL disabling options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# Browser variable setting the browser driver and utilising options as above. 
# * Note the path needs to be modified depending where
# ...this script is run from
browser = webdriver.Chrome(ChromeDriverManager().install())


def newsletter_url(urlinput):
    browser.get(urlinput)

def get_data():

    data = []
    
    data_chunks = browser.find_elements_by_xpath(
        '//tbody//*[text()[contains(.,"Massive Fundings")]]/ancestor::tbody[1]//span[@*="font-family:verdana,geneva,sans-serif"] | //tbody//*[text()[contains(.,"Massive Fundings")]]/ancestor::tbody[1]//span[@*="font-family:verdana,geneva,sans-serif;"]')
    # print(data_chunks)
    for iteration, data_chunk in enumerate(data_chunks):

        print("Processing company " + data_chunk.text.split(',')[0] + ". Data chunk " + str(iteration+1) + "...")
        codata = {
            'Startup Name': "",
            'Startup Notes': "",
            'Article URL': "",
            'Scrape Status': "Scraped & Waiting"
        }
        
        codata["Startup Name"] = data_chunk.text.split(',')[0]
        codata["Startup Notes"] = data_chunk.text

            # time.sleep(3)
        chunk_links = data_chunk.find_elements_by_xpath('descendant::a')
        if not chunk_links:
            print("No link(s) found")
            data.append(codata)
            print(codata)
            continue
        else:
            for link in chunk_links:
                thehref = link.get_attribute("href")
                browser.execute_script("window.open('');")
                browser.switch_to.window(browser.window_handles[1])
                browser.get(thehref)
                time.sleep(1)
                if "consent.yahoo.com" in browser.current_url:
                    browser.find_element_by_xpath('//button[@name="agree"]').click()
                    codata["Article URL"] = browser.current_url
                else:
                    codata["Article URL"] = browser.current_url    
                browser.close()
                browser.switch_to.window(browser.window_handles[0])
        data.append(codata)
        print(codata)
    browser.quit()
    print(data)
    return data

def scrape(input_url_here):
    newsletter_url(input_url_here)
    return get_data()
