import bs4
import requests

headers = {
    'User-Agent': 'Not_Crawling X)'
}
response = requests.get('https://www.melon.com', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')

songs = soup.select('.on.nth1 > .list_wrap.typeRealtime>ul>.rank_item')

with open('melon_rank_1.csv', 'w') as f:
    for song in songs:
        title = song.select_one('div.rank_cntt > div.rank_info > p.song > a').text
        artist = song.select_one('div.rank_cntt > div.rank_info > div.artist > div.ellipsis > a').text
        f. write(f'{title},{artist}\n')