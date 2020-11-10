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

# Import mailmonitor module
import emailmonitor.emailmonitor as emailextractor


# Import Airtable API actions for table "Startups"
import airtableapi.airtableapi_startups as airtable_startups

import schedule
import time

def scrape():

    # Print to console to signify scrape script started
    print("Scraping script running now...")

    # Get the latest unseen mail. Returns the filename as a string
    print("Checking for new StrictlyVC emails...")
    newsletter = emailextractor.getunseen(gmail_user,gmail_pw,imap_server,
        imap_label)

    if not newsletter:
        print("No email detected - terminating until next run...")
        return
    else:

        # Import StrictlyVC newsletter scraping module
        import scrape_scripts.scrape_strictlyvc as strictlyvc

        # Single parameter must be the location of the HTML StrictlyVC email...
        # Has to work with Google Chrome URL path...
        #... returns one list with dictionary objects for each company info block
        strictly_vc_data = strictlyvc.scrape(
            newslet_scrape_path +
            f'{newsletter}.html')

        # # # Add records to Airtable table "Startups"
        airtable_startups.add_records(airtable_apikey,
        airtable_base,airtable_table,strictly_vc_data)
scrape()
# schedule.every(30).minutes.do(scrape)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
