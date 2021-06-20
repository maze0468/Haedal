import bs4
import requests
import csv

headers = {
    '(User-Agent': 'Not_Crawling X)'
}
response = requests.get('https://kin.naver.com/', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')

ranks = soup.select('#rankingChart > ul > li')

with open('kin_rank_f.csv', 'w') as f:
    writer = csv.writer(f, delimiter=",", quotechar='"')
    for rank in ranks:
        num = rank.select_one('span.no').text
        title = rank.select_one('a.ranking_title').text
        f.write(f'{num}위,{title}\n')
