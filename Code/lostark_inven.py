from bs4 import BeautifulSoup
import requests
import pandas as pd

result = {'date' : [],
          'title' : [],
          'content' : []}

print('수집 시작')

for j in range(2):
    p = requests.get('https://www.inven.co.kr/board/lostark/5352?p=' + str(j))
    soup = BeautifulSoup(p.text, 'html.parser')

    selection = soup.select('a.subject-link')

    for i in range(len(selection)):
        title = selection[i].text.replace("\xa0[밸런스]\xa0\xa0","")
        url = selection[i].get('href')

        q = requests.get(url)
        soup2 = BeautifulSoup(q.text, 'html.parser')

        content = soup2.select('div#powerbbsContent')[0].text
        date = soup2.select('div.articleDate')[0].text

        result['date'].append(date)
        result['title'].append(title)
        result['content'].append(content)

print('수집 완료')

final = pd.DataFrame(result)
final.to_excel('balance_text.xlsx', index = False)

print('파일 저장 완료')
