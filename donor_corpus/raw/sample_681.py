# Write a script that generates daily edit AND view counts for Panama Papers over its first 30 days of existence, and prints them to a CSV or TSV file in reverse-chronological order. You file should have three colums with the headers "date", "edits" and "views".

import csv
import json
import requests
import operator
from urllib.parse import quote

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Panama_Papers',
               'format' : 'json',
               'rvdir' : 'newer',
               'rvstart': '2016-04-03T17:59:05Z',
               'rvend' : '2016-05-03T00:00:00Z',
               'rvlimit' : 500,
               'continue' : '' }

days = {}
done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()
    pages = response['query']['pages']
    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        for rev in revisions:
            revday = rev['timestamp'][:10].replace("-","")
            revhour = rev['timestamp'][11:13]            
            if revday in days.keys():
                if revhour in days[revday].keys():
                    days[revday][revhour] += 1
                else:
                    days[revday][revhour] = 1
            else:
                days[revday] = {}
                days[revday][revhour] = 1

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True

# print(days)
for dkey, dval in days.items():
    daily_edits = 0
    for hkey, hval in dval.items():
        daily_edits += hval
    days[dkey]['total'] = daily_edits

# print(days)

ENDPOINT = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/'

wp_code = 'en.wikipedia'
access = 'all-access'
agents = 'all-agents'
page_title = 'Panama Papers'
period = 'daily'
start_date = '20160403'
end_date = '20160502'

wp_call = requests.get(ENDPOINT + wp_code + '/' + access + '/' + agents + '/' + quote(page_title, safe='') + '/' + period + '/' + start_date + '/' + end_date)
response = wp_call.json()

# print(json.dumps(response, indent=4))

for dv in response['items']:
#     print(dv['timestamp'])
    ts = dv['timestamp'][:-2]
    if ts in days.keys():
        days[ts]['views'] = dv['views']

# print(json.dumps(days, indent=4))

days_sorted = sorted(days.items(), key=operator.itemgetter(0), reverse=True)
print(days_sorted)

with open('pp30days_views_edits.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('date', 'edits', 'views'))
    for n in days_sorted: 
        writer.writerow((n[0], n[1]['total'], n[1]['views'],))