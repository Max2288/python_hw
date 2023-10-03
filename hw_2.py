import requests
import json
from bs4 import BeautifulSoup


HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
games = {}

for page in range(1, 16):
    url = f"https://zaka-zaka.com/game/new/page{page}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        container = soup.find("div", class_="tabs-content tab-1 active")
        games = container.find_all("a", class_="game-block")
        for game in games:
            try:
                name = game.find("div", class_="game-block-name").text
                price = game.find("div", class_="game-block-price").text
                games[name] = " ".join(
                    price.replace("c", "Рубли моё всё").strip().split()
                )
            except Exception as err:
                print(err)

with open('zaka_zaka.json', 'w', encoding='utf-8') as json_file:
    json.dump(games, json_file, ensure_ascii=False, indent=4)
