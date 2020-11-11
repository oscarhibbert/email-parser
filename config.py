# Xpath for each "section" for extraction in the email
xpath_locator = {
    'section_location': '//tbody//*[text()[contains(.,"Massive Fundings")]]/ancestor::tbody[1]//span[@*="font-family:verdana,geneva,sans-serif"] | //tbody//*[text()[contains(.,"Massive Fundings")]]/ancestor::tbody[1]//span[@*="font-family:verdana,geneva,sans-serif;"]',
} 


# Customise this function to point to where to fetch each "section" title
def extract_section_title(section):
    title = section.split(',')[0]
    return title


# The name of each Airtable field you have used. Note this is limited to
# fields below (Title, Text, Link & Status):
airtable_record_model = {
    # Title of email section e.g. "Startup Name"
    'field_section_title': "Startup Name",
    # Email section body text e.g. "Startup Notes"
    'field_section_text': "Startup Notes",
    # Email section href (only supports 1 href at this time) e.g. "Article URL"
    'field_section_link': "Article URL",
    # Status field. Will populate with "Parsed from Email" for each record e.g. 
    # "Status"
    'field_status': "Status"
}
