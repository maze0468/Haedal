import bs4
import requests
import csv

headers = {
    '(User-Agent': 'Not_Crawling X)'
}
response = requests.get('https://kin.naver.com/', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')

ranks = soup.select('#rankingChart > ul > li')

num_2 = lambda rank : int(rank.select_one('span.no').text)
title_2 = lambda rank: (rank.select_one('a.ranking_title').text)

with open('kin_rank_.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['num', 'title'])
    for rank in sorted(ranks, key=num_2):
        num = num_2(rank)
        title = title_2(rank)
        writer.writerow([f'{num}위,{title}\n'])
