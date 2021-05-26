import bs4 #pip install bs4
import requests #pip install requests

headers = {
    'User-Agent': 'Not_Crawling X)'
}
response = requests. het('https://www.melon.com', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')

songs = soup.select('.on.nth1 > .list_warp.typeRealtime>ul>.rank_item')

with open('melon_rank.csv','w') as f:
    for son in songs:
        title = song.select_one('div.rank_cntt > div.rank_number > span.rank').text
        artists = sond.select_ont('div.rank_cntt > div.rank_info > div.artist > div.ellipsis > a').text
        f. write(f'{title},{artist}'\n)