#helper functions for marketCommands

import re
import requests
import json
import time
from datetime import datetime, timedelta
import sys
axie_endpoint = "https://graphql-gateway.axieinfinity.com/graphql"
query_for_walletpy_key = "almost leaked my key here oops"

def get_axieIdstring_from_list(axieIds_list):
    axieIds_string = [str(num) for num in axieIds_list]
    return axieIds_string
        
def get_axieIdstring_from_txt(filename):
    with open(filename, 'r') as file:
        file_contents = file.read()
    axieIds = re.findall(r'\d{2,20}', file_contents)
    axieIds_string = list(map(str, axieIds))
    return axieIds_string

def grab_incubated_list(owner_address):
    ronin = owner_address.replace("ronin:", "0x")
    query = """
    query MyQuery {
    axies(
        auctionType: All
        criteria: {stages: 1}
        owner: "%s"
        size: 1000
    ) {
        results {
        id
        birthDate
        }
        total
    }
    }
    """ % ronin
    r = response = requests.post(axie_endpoint, json={"query": query})
    response = json.loads(r.text)
    response_data = response["data"]["axies"]["results"]
    axie_list = []
    for axie_data in response_data:
        axie_id = axie_data["id"]
        birth_date = axie_data["birthDate"]
        axie_info = [axie_id, birth_date]
        axie_list.append(axie_info)
    current_datetime = datetime.now()
    fivedaysago = current_datetime - timedelta(days=5)
    unix_fivedaysago = int(fivedaysago.timestamp())
    incubatedlist = []
    for axie in axie_list:
        axieId = axie[0]
        birthDate = axie[1]
        if(unix_fivedaysago > birthDate):
            incubatedlist.append(axieId)
    return incubatedlist


