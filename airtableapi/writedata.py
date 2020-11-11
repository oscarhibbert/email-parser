# Airtable setup
from airtable import Airtable


def add_records(apikey,base,table,inputlisthere):

    airtable = Airtable(base,table,api_key=apikey)

    print("\nPushing records to Airtable. Batches of 5 records per second...\n")
    airtable.batch_insert(inputlisthere, typecast=False)
    print("\n✅ Records pushed to Airtable successfully!\n")
