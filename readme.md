# Email Parser

A python application that decodes & extracts MIME raw email messages via IMAP into cleanly formatted Airtable records which include separate data points.

![Email Parser in action](https://images.squarespace-cdn.com/content/v1/5f68900ab0847f6b53d3b288/1605056165374-178PDTE0PK5Y4TKGVIQ1/ke17ZwdGBToddI8pDm48kNvT88LknE-K9M4pGNO0Iqd7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1USOFn4xF8vTWDNAUBm5ducQhX-V3oVjSmr829Rco4W2Uo49ZdOtO_QXox0_W7i2zEA/email-parser.jpg)

## Installation

This application is tested with Python 3.7.

1. Using git ``` $ git clone https://github.com/oscarhibbert/email-parser```

2. Navigate to the app directory ```$ cd email-parser```

3. Install all dependencies using pipenv ```$ cd pipenv install```


## Configuration

1. Create a free Airtable account [here](https://airtable.com/signup).

2. Create a new Airtable base, table & view. See [here](https://support.airtable.com/hc/en-us/articles/360021518753-Getting-started-starting-with-the-base-ics).

3. Add your Airtable fields in ```config.py```. **This is limited to the fields given in ```config.py```**

4. Add your xpath locator for selecting each email section you want to extract in ```config.py```.

5. Add your logic to fetch the title of each email section ```config.py```.

6. Create an environment variable ```.env``` file in the application directory with the following config:

```
# 1. IMAP information. The application will fetch the latest unread email
# under the IMAP label specified
IMAP_USER = ''
IMAP_PW = ''
IMAP_SERVER = ''
IMAP_LABEL = ''


# 2. Airtable credentials
AIRTABLE_APIKEY = ''
AIRTABLE_BASE = ''
AIRTABLE_TABLE = ''
```


## Running the Application

From the app directory ```$ pipenv run python3 emailparser.py```


## Limitations

* Can only process one email at a time.


## Final Note

This app works great when run in the background by [launchd](https://www.launchd.info/) the process used by MacOS to manage  daemons and agents.

