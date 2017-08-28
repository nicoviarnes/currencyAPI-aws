import urllib
import urllib.request
from bs4 import BeautifulSoup
import json


def lambda_handler(event, context):
    
    print( "Code Running.........")
    

    league = 'Harbinger'
    want = event['want']
    have = event['have']
    if have == '4':
        curHave = "Chaos"

    if want == '6':
        curWant = "Exalted"

    poe = urllib.request.urlopen('http://currency.poe.trade/search?league='+league+'&online=x&want='+want+'&have='+have).read()
    soup = BeautifulSoup(poe, "html.parser")

    listings = soup.find_all('div', class_ = 'displayoffer')
    print(listings)
    cNames = soup.find_all('div', class_ = 'large-3.small-3.columns.currency')
    jdata = {}
    i = 0
    while i < 10:
        ign = listings[i]['data-ign']
        buyVal = listings[i]['data-buyvalue']
        sellVal = listings[i]['data-sellvalue']
        simVal = float(buyVal)/float(sellVal)
        i+=1

        jdata['ign'] = ign
        jdata['rate'] = str(simVal) +':1'
        jdata['have'] = curHave
        jdata['want'] = curWant
        json_data = json.dumps(jdata)
        print(json_data)