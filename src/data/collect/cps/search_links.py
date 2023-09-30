import requests
from bs4 import BeautifulSoup, SoupStrainer

from src.share.assert_throw import ASSERT_THROW

def searchLinks():
    workDayURL = ''
    workDayLinks = []
    saturdayURL = ''
    saturdayLinks = []
    sundayURL = ''
    sundayLinks = []

    payload = {
        'pojam': 'zetovci'
    }

    searchComplete = False
    while not searchComplete:
        try:
            with requests.Session() as s:
                p = s.post('https://www.zet.hr/interno/default.aspx?a=login',
                           data=payload)
                r = s.get('https://www.zet.hr/interno/default.aspx?id=1041')
                content = r.content

                notificationsLinks = []
                for line in BeautifulSoup(content,
                                          parse_only=SoupStrainer('a')):
                    if hasattr(line, "href"):
                        link = line['href']
                        print(link)
                        # notifications
                        if ('dubrava/' in link):
                            notificationsLinks.append({'URL': link, 'name': line.text})

                        if('RD' in link or 'Radni dan' in line.text or 'radni dan' in line.text):
                            workDayLinks.append({'URL': link, 'name': line.text})
                            #workDayURL = link
                        if('SUB' in link or 'S_internet' in link or 'ubot' in line.text):
                            print('what')
                            saturdayLinks.append({'URL': link, 'name': line.text})
                            #saturdayURL = link
                        if('NED' in link or 'N_internet' in link or 'edjelj' in line.text):
                            sundayLinks.append({'URL': link, 'name': line.text})
                            #sundayURL = link
            searchComplete = True
        except Exception as e:
            TRACE(e)

    ASSERT_THROW(len(workDayLinks) > 0, 'Nije nadjeno rasporeda za radne dane.')
    ASSERT_THROW(len(saturdayLinks) == 1, 'Nadjeno 0 ili vise subotnjih rasporeda.')
    ASSERT_THROW(len(sundayLinks) == 1, 'Nadjeno 0 ili vise nedeljnih rasporeda.')
    return {'workDay': workDayLinks,
            'saturday': saturdayLinks,
            'sunday': sundayLinks,
            'notificationsLinks': notificationsLinks}
