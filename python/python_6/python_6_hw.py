import bs4
import requests
import csv

headers = {
    'User-Agent': 'Not_Crawling X'
}
response = requests.get('https://kin.naver.com/', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')

ranks = soup.select('#rankingChart > ul > li')

num = lambda rank : int(rank.select_one('span.no').text)
title = lambda rank: (rank.select_one('a.ranking_title').text)

with open('kin_rank_.csv', 'w') as f:
    writer = csv.writer(f)

    for rank in sorted(ranks, key=num):
        num2 = num(rank)
        title2 = title(rank)
        writer.writerow([f'{num2}위',title2])
