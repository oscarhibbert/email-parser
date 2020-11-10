# Airtable setup
from airtable import Airtable


def add_records(apikey,base,table,inputlisthere):

    airtable = Airtable(base,table,api_key=apikey)

    print("Pushing records to Airtable. Batches of 5 records per second...")
    airtable.batch_insert(inputlisthere, typecast=False)
    print("✅ Records pushed successfully!")
