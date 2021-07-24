import requests
from bs4 import BeautifulSoup
import math
import re
# import lxml


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
}

login_data = {
    'Email': 'sajjadshokrgozar77@gmail.com',
    'Password': '137700SH',
}
with requests.Session() as s:
    url = 'https://iranfile.ir/User/Login'
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    login_data['__RequestVerificationToken'] = soup.find('input', attrs={'name': '__RequestVerificationToken'})['value']
    r = s.post(url, data=login_data, headers=headers)
    # print(r.url)



# get file content
urlFile = open('urls.txt', 'r', encoding='utf8')
urls = urlFile.read()
urlFile.close()

urlList = urls.split('\n')

for url in urlList:
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    totalRowsText = soup.find('p', {'id': 'total-rows'}).text
    # print(totalRowsText)

    for c in totalRowsText.split():
        if c.isdigit():
            totalRows = int(c)

    totalPages = math.ceil(totalRows / 20)

    pagefirsturl = re.search('((https:\/\/iranfile.ir\/Search\/).*-)(.*)\/', url)
    pagesecondurl = re.search('-([0-9]+\/)(.*)', url)

    for num in range(1, totalPages + 1):
        pageUrl = str(pagefirsturl[1] + str(num) + '/' + pagesecondurl[2])
        # print(pageUrl)
        r = requests.get(pageUrl)

        soup = BeautifulSoup(r.text, 'html.parser')
        trs = soup.find('tbody').find_all('tr')
        # print(trs)
        for tr in trs:
            a = tr.find('a', href=True)

            urlFile = open('singlePagesUrl.txt', 'a', encoding='utf8')
            urlFile.write(a['href'] + '\n')
            urlFile.close()

            # print(a['href'])
