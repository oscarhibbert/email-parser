# Airtable setup
from airtable import Airtable


def add_records(apikey,base,table,inputlisthere):

    # airtable = Airtable(base_key, table_name, api_key='yourapikey')
    # Airtable table Startups configuration
    airtable = Airtable(base,table,api_key=apikey)

    print("Pushing to Airtable table Startups via API. Batches of 5 records per second...")
    airtable.batch_insert(inputlisthere, typecast=False)
    print("✅ Records pushed successfully!")
