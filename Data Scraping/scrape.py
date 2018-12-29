"""

Before running the program ensure:

1. Variables <keyw> and <number_i> are set accordingly (refer the website: https://linux.die.net/man/).





"""



keyw = 'keyword_containing_sufficient_data'
number_i = "manual_number"





url_final = "https://linux.die.net/man/"+number_i+ "/"



import requests
from bs4 import BeautifulSoup
import csv
import time
import requests









page = requests.get(url_final)
soup = BeautifulSoup(page.text, 'html.parser')
f = csv.writer(open('cmd-names.csv', 'w'))
f.writerow(['Name', 'Link'])


cmd_name_list = soup.find("div", {"id": "content"})
cmd_name_list_items = cmd_name_list.find_all('a')


for cmd_name in cmd_name_list_items:
    names = cmd_name.contents[0]
    links = url_final + cmd_name.get('href')
    print(names)
    print(links)
    f.writerow([names, links])


import urllib.request
import json
from urllib.request import Request, urlopen


request = Request(url_final+keyw, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html,'html.parser')
for script in soup(["script", "style"]):
    script.decompose()


try:
    name = soup.find('h2', text='Name').next_sibling.string
except:
    name = ''

synopsis = soup.find('h2', text='Synopsis').next_sibling.string


print(name)

soup.find('h2',text='Synopsis').find_next_sibling('h2').string


def between(cur, end):
    while cur and cur != end:
        if isinstance(cur, NavigableString):
            text = cur.strip()
            if len(text):
                yield text
        cur = cur.next_element


from bs4 import BeautifulSoup, NavigableString
print(' '.join(text for text in between(soup.find('h2', text='Synopsis').next_sibling,
                                        soup.find('h2',text='Synopsis').find_next_sibling('h2'))))




try:
    synopsis = ' '.join(text for text in between(soup.find('h2', text='Synopsis').next_sibling,
                                            soup.find('h2',text='Synopsis').find_next_sibling('h2')))
except:
    synopsis = ''



try:
    description = ' '.join(text for text in between(soup.find('h2', text='Description').next_sibling,
                                        soup.find('h2',text='Description').find_next_sibling('h2')))
except:
    description = ''


try:
    options = ' '.join(text for text in between(soup.find('h2', text='Options').next_sibling,
                                        soup.find('h2',text='Options').find_next_sibling('h2')))
except:
    options = ''




try:
    see_also = ' '.join(text for text in between(soup.find('h2', text='See Also').next_sibling,
                                        soup.find('h2',text='See Also').find_next_sibling('h2')))
except:
    see_also = ''


see_also


try:
    referenced_by = ' '.join(text for text in between(soup.find('h2', text='Referenced By').next_sibling,
                                        soup.find('h2',text='Referenced By').find_next_sibling('h2')))
except:
    referenced_bby = ''


synopsis


def between(cur, end):
    while cur and cur != end:
        if isinstance(cur, NavigableString):
            text = cur.strip()
            if len(text):
                yield text
        cur = cur.next_element




def find_data(page_url):
    import urllib.request
    from bs4 import BeautifulSoup, NavigableString
    import json
    from urllib.request import Request, urlopen
    request = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html,'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    try:
        name = ' '.join(text for text in between(soup.find('h2', text='Name').next_sibling,
                                                soup.find('h2',text='Name').find_next_sibling('h2')))
    except:
        name = ''
    try:
        synopsis = ' '.join(text for text in between(soup.find('h2', text='Synopsis').next_sibling,
                                                soup.find('h2',text='Synopsis').find_next_sibling('h2')))
    except:
        synopsis = ''
    try:
        description = ' '.join(text for text in between(soup.find('h2', text='Description').next_sibling,
                                            soup.find('h2',text='Description').find_next_sibling('h2')))
    except:
        description = ''
    try:
        options = ' '.join(text for text in between(soup.find('h2', text='Options').next_sibling,
                                            soup.find('h2',text='Options').find_next_sibling('h2')))
    except:
        options = ''
    try:
        see_also = ' '.join(text for text in between(soup.find('h2', text='See Also').next_sibling,
                                            soup.find('h2',text='See Also').find_next_sibling('h2')))
    except:
        see_also = ''
    try:
        referenced_by = ' '.join(text for text in between(soup.find('h2', text='Referenced By').next_sibling,
                                            soup.find('h2',text='Referenced By').find_next_sibling('h2')))
    except:
        referenced_by = ''
        
    data = {
        'name':name,
        'synopsis':synopsis,
        'description':description,
        'options':options,
        'see_also':see_also,
        'referenced_by':referenced_by
    }
    return data

find_data(url_final+keyw)


extracted_data = []
f = csv.writer(open('data.csv', 'w'))
f.writerow(['Name', 'Synopsis','Description','Options','See Also','Referenced By'])


      
        


iterator = 0

def write_final():
    global iterator
    number_1 = len(cmd_name_list_items)
    while iterator != 19992:
        cmd_name = cmd_name_list_items[iterator]
        url = url_final + cmd_name.get('href')
        print('Extracting data from %s'%url)
        #Lets wait for 5 seconds before we make requests, so that we don't get blocked while scraping. 
        #if you see errors that say HTTPError: HTTP Error 429: Too Many Requests , increase this value by 1 second, till you get the data. 
        extracted_data.append(find_data(url))
        data = find_data(url)
        Name = data['name']
        Synopsis = data['synopsis']
        Description = data['description']
        Options = data['options']
        see_also = data['see_also']
        referenced_by = data['referenced_by']
        f.writerow([Name, Synopsis,Description,Options,see_also,referenced_by])
        print("Written:")
        print(iterator)
        iterator += 1





        
        




def final_catch():
    try:
        write_final()
    except Exception:
        print("will sleep for "+ "10"  + " seconds")
        time.sleep(10)
        # try again
        final_catch()
    finally:
        try:
            cleanup()
        except:
            pass



final_catch()
