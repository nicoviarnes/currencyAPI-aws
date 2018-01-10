import urllib
import urllib.request
from bs4 import BeautifulSoup
import json
def lambda_handler(event, context):
    league = event['league']
    want = event['want']
    have = event['have']
    poe = urllib.request.urlopen('http://currency.poe.trade/search?league='+league+'&online=x&want='+want+'&have='+have).read()
    soup = BeautifulSoup(poe, 'html.parser')
    listings = soup.find_all('div', class_ = 'displayoffer')
    cNames = soup.find_all('div', class_ = 'large-3.small-3.columns.currency')
    jdata = {}
    json_data = {}
    i = 0
    if listings:
        while i < len(listings):
            ign = listings[i]['data-ign']
            buyVal = listings[i]['data-buyvalue']
            sellVal = listings[i]['data-sellvalue']
            simVal = float(buyVal)/float(sellVal)
            i+=1
            jdata['ign'] = ign
            jdata['rate'] = str(simVal) +':1'
            json_data[i] = json.dumps(jdata)
        return json_data
    else:
        return ('Nothing found.')
