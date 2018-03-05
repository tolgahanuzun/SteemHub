import requests
from bs4 import BeautifulSoup

# https://steemd.com/@tolgahanuzun

URL = 'https://steemd.com/'

def hook_activity(username):
    if not username.startswith('@'):
        username = '@' + username
    hook = requests.get("{}{}".format(URL, username))
    
    hook_parse = BeautifulSoup(hook.text, 'html.parser')
    datas = hook_parse.find('div', {"class": "col-md-8"})
    html_result = []

    for data in datas.find_all('div', {"class": "op"})[:30]:
        find_data = data.find('span')
        if not find_data.find('table'):
            # temp = find_data.a.get('href')
            # find_data.a = '<a href="https://steemit.com{}">{}</a>'.format(temp, temp.replace('/@',''))
            html_result.append(find_data)
        else:
            parse_comment = find_data.contents[2].replace(' ','').replace('\n','')
            if parse_comment == 'comment_options':
                author = find_data.find('table').contents[0].find('span').text
                permalink = find_data.find('table').contents[1].find('span').text
                result_url = '@{}/{}'.format(author, permalink)
                result_html = '<a href="{}">{}</a>'.format(result_url, permalink)
                html_result.append(find_data.contents[1].text + ' comment ' + result_html)
            else:
                pass
    return html_result

def hook(name):
    datas = hook_activity(name)

    result = []
    for data in datas:
        if str(data) == '<span class="tag tag-virt">virtual</span>':
            pass
        else:
            result.append(str(data).replace('href="/', 'href="https://steemit.com/'))
        
    return result

def feed_list(username):
    url = 'https://api.steemjs.com/get_account_history?account={}&from=100000&limit=100'
    username_feed = url.format(username)
    return requests.get(username_feed).json()
    

