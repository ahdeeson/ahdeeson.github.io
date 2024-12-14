import requests
import easygui
from bs4 import BeautifulSoup

def get_events(url):
    event_page = requests.get(url) #get page from http request
    soup = BeautifulSoup(event_page.content, 'html.parser') #parse response

    row = soup.table.tbody.tr.next_sibling.next_sibling #navigate to table row of the first event
    events = [] #init array for event titles

    while row: #while there are still rows
        title = row.contents[7].string #get title from row
        events.append(title) #add title to array
        row = row.next_sibling.next_sibling #navigate to next row, skipping the blank
        
    return events

def get_entries(url):
    event_page = requests.get(url) #get page from http request
    soup = BeautifulSoup(event_page.content, 'html.parser') #parse response
    print(soup.table)

act_regatta = "https://www.regattacentral.com/regatta/?job_id=8787"
regatta_url = "https://www.regattacentral.com/regatta/events/?job_id=9216&org_id=0"
event_url = "https://www.regattacentral.com/regatta/entries/competitors/?job_id=8787&event_id="

print(get_entries(event_url + "2"))

# event_titles = get_events(regatta_url)
# # print(event_titles)
# save_folder = easygui.diropenbox()

# for event_n in range(1, len(event_titles) + 1):
#     entries = get_entries(event_url + event_n)