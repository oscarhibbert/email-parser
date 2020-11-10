# Load & print datetime
from datetime import datetime
print('\nScript started @ ' +
      str(datetime.now()) + '\n')


# Load credentials & other env data
from dotenv import load_dotenv
import os

airtable_apikey = os.environ.get('AIRTABLE_APIKEY')
airtable_base = os.environ.get('AIRTABLE_BASE')
airtable_table = os.environ.get('AIRTABLE_TABLE')

gmail_user = os.environ.get('GMAIL_USER')
gmail_pw = os.environ.get('GMAIL_PW')
imap_server = os.environ.get('IMAP_SERVER')
imap_label = os.environ.get('IMAP_LABEL')

newslet_scrape_path = os.environ.get('NEWSLET_SCRAPE_PATH')


# Import email monitor module
import emailmonitor.fetchemail as fetchemail


# Import Airtable API actions for Airtable table
import airtableapi.getdata as airtable_getdata


def scrape():

    # Print to console to signify email parser started
    print("\nEmail parser running now...\n")

    # Get the latest unseen email. Returns the filename as a string
    print("\nChecking for latest unread email under specified label...\n")
    email_htmlversion = fetchemail.getunseen(gmail_user, gmail_pw, imap_server,
        imap_label)

    if not email_htmlversion:
        print("\nNo email detected - terminating until next run...\n")
        return
    else:

        # Import data extractor module
        import dataextractor.extractdata as extractdata
        # Import os for finding tempdata absolute path
        import os
        
        # The following code extracts data from HTML version of the email. 
        # Path must be absolute as Google Chrome can only accept an 
        # absolute path to the file to load it.
        tempdata_abspath = os.path.abspath('./tempdata').replace(" ", "%20")
        extracted_data = extractdata.scrape(
            'file:///' + tempdata_abspath + '/' + f'{email_htmlversion}.html')    

        # This code deletes the email HTML file from the tempdata directory
        filepath = './tempdata/' + f'{email_htmlversion}.html'
        try:
            os.remove(filepath)
            print("\nHTML email file deleted from the 'tempdata' directory", 
            "sucessfully.\n")
        except OSError as e:
            print("Error: %s : %s" % (filepath, e.strerror))
        
        # This code takes the returned data from extraction & pushes it
        # to Airtable as configured in config.py
        airtable_getdata.add_records(airtable_apikey,
        airtable_base,airtable_table,extracted_data)

scrape()
