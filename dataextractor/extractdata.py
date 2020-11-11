# Import deps
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import json

# Import & load config
import config
xpath = config.xpath_locator['section_location']
airtable_record_model = config.airtable_record_model


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


def email_url(urlinput):
    browser.get(urlinput)

def get_data():

    data = []
    
    data_chunks = browser.find_elements_by_xpath(xpath)
    # print(data_chunks)
    for iteration, data_chunk in enumerate(data_chunks):

        print("\nProcessing email section", str(iteration+1) + ". Title:",
              data_chunk.text.split(',')[0] + "...\n")
        codata = {
            airtable_record_model['field_section_title']: "",
            airtable_record_model['field_section_text']: "",
            airtable_record_model['field_section_link']: "",
            airtable_record_model['field_status']: "Parsed from Email"
        }
        
        codata[airtable_record_model['field_section_title']
               ] = config.extract_section_title(data_chunk.text)
        codata[airtable_record_model['field_section_text']] = data_chunk.text

            # time.sleep(3)
        chunk_links = data_chunk.find_elements_by_xpath('descendant::a')
        if not chunk_links:
            print("\nNo href link found\n")
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
                # Logic for handling Techcrunch cookie redirect
                if "consent.yahoo.com" in browser.current_url:
                    browser.find_element_by_xpath('//button[@name="agree"]').click()
                    codata[airtable_record_model['field_section_link']
                           ] = browser.current_url
                else:
                    codata[airtable_record_model['field_section_link']
                           ] = browser.current_url
                browser.close()
                browser.switch_to.window(browser.window_handles[0])
        data.append(codata)
        print(codata)
    browser.quit()
    return data

def scrape(input_url_here):
    email_url(input_url_here)
    return get_data()
